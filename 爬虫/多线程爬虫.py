#多线程爬虫
"""分析：
    两类线程：下载、解析
    内容队列：下载线程网队列中put数据，解析线程从队列get数据
    url队列：下载线程从url队列get数据
    写数据：上锁"""
import threading
import time
from queue import Queue
from lxml import etree
import requests
import json
#用来存放采集线程
crawl_list = []
#用来存放解析线程
parser_list = []
class CrawlThread(threading.Thread):
    def __init__(self, name, page_queue, data_queue):
        super(CrawlThread, self).__init__()
        self.name = name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.url = 'http://www.fanjian.net/jiantu-{}'
        self.headers = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        }
    def run(self):
        print('%s-----线程启动' % self.name)
        while 1:
            #判断采集线程合适退出
            if self.page_queue.empty():
                break
            #从队列中取出页码
            page = self.page_queue.get()
            #拼接url，发送请求
            url = self.url.format(page)
            r = requests.get(url=url, headers=self.headers)
            #将响应放入队列data_queue
            self.data_queue.put(r.text)
            print(r.url)
        print('%s-----线程结束' % self.name)
class ParserThread(threading.Thread):
    def __init__(self, name, data_queue, fp, lock):
        super(ParserThread, self).__init__()
        self.name = name
        self.data_queue = data_queue
        self.fp = fp
        self.lock = lock
    def run(self):
        print('_____')
        while 1:
            #判断什么时候退出
            """if self.data_queue.empty():
                break"""
            #从data_queue中取出数据
            try:
                data = self.data_queue.get(True, 10)
            #解析数据
                self.parse_content(data)
            except Exception as e:
                break
        print('*'*10)
    
    def parse_content(self, data):
        print('解析。。。。。。。。。。。。。')
        tree = etree.HTML(data)
        #获取图片标题
        li_list = tree.xpath('//ul[@class="cont-list"]/li')
        #获取图片url
        items = {}
        for oli in li_list:
            #获取标题
            title = oli.xpath('.//h2/a/text()')[0]
            #获取去图片链接
            image_url = oli.xpath('.//div[@class="cont-list-main"]/p/img/@data-src')
            item = {
                '标题':title, 
                '链接':image_url,
            }
            items.append(item)
        self.lock.acquire()
        self.fp.write(json.dumps(items, ensure_ascii = False + '\n'))
        self.lock.release()
        print(items[0])
def create_queue():
    #创建一个页码队列
    page_queue = Queue()
    for page in range(1, 6):
        page_queue.put(page)
    #创建内容队列
    data_queue = Queue()
    return page_queue, data_queue
#创建采集线程
def create_crawl_thread(page_queue, data_queue):
    crawl_name = ['采集线程1号', '采集线程2号', '采集线程3号']
    for name in crawl_name:
        tcrawl = CrawlThread(name, page_queue, data_queue)
        crawl_list.append(tcrawl)
        print('添加url')
#创建解析线程
def create_parser_thread(data_queue, fp, lock):
    print("解析！！！开始")
    crawl_name = ['解析线程1号', '解析线程2号', '解析线程3号']
    for name in crawl_name:
        tparser = ParserThread(name, data_queue, fp, lock)
        parser_list.append(tparser)
def main():
    #1、创建队列
    page_queue, data_queue = create_queue()
    #打开文件
    fp = open('jian.json', 'a', encoding='utf8')
    lock = threading.Lock()
    #2、创建采集线程
    create_crawl_thread(page_queue, data_queue)
    #3、创建解析线程
    create_parser_thread(data_queue, fp, lock)
    #启动线程
    for tcrawl in crawl_list:
        tcrawl.start()
    #启动解析线程
    time.sleep(10)
    for tparser in parser_list:
        tparser.start()
    print('解析进程开始')
    #主线程等待子线程结束
    for tcrawl in crawl_list:
        tcrawl.join()
    for tparser in parser_list:
        tparser.join()
if __name__ == '__main__':
    main()