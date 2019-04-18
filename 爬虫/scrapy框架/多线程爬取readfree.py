import requests
import threading
from lxml import etree
import urllib.request
import pymongo
import json
import time
#get post get
crawl_list = []
store_list = []
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

"""class CrawlThread(threading.Thread):
    def __init__(self):
        super(CrawlThread, self).__init__()
        pass

    def run(self):
        pass
class Store_Thread(threading.Thread):
    def __init__(self):
        super(Store_Thread, self).__init__()
        pass
    def run(self):
        pass"""

def code_download(s):
    url = 'https://readfree.me'
    response = s.get(url, headers = headers)
    tree = etree.HTML(response.text)
    #下载验证码手工输入
    image_src = 'https://readfree.me' + tree.xpath('//img[@class="captcha"]/@src')[0]
    urllib.request.urlretrieve(image_src, 'readfree验证码.png')
    csrfmiddlewaretoken = tree.xpath('//form[@id="id_signin_form"]/input[1]/@value')[0]
    captcha_0 = tree.xpath('//input[@id="id_captcha_0"]/@value')[0]
    captcha_1 = input("请输入验证码：")
    return csrfmiddlewaretoken, captcha_0, captcha_1

def login(s, csrfmiddlewaretoken, captcha_0, captcha_1):
    post_url = 'https://readfree.me/auth/login/?next=/'
    form_data = {
        'csrfmiddlewaretoken':csrfmiddlewaretoken,
        'login': '332138569@qq.com',
        'password':'lichao3335390',
        'captcha_0':captcha_0,
        'captcha_1':captcha_1
    }
    response = s.post(url=post_url, headers=headers, data=form_data)
    return response
def create_crawl_thread(data_queue):
    pass
def create_store_thread(data_queue):
    pass
def parsr_url(s, down_url):
    resp = s.get(url=down_url, headers=headers)
    url = etree.HTML(resp.text).xpath('//a[@class="book-down btn btn-mini btn-success"]/@href')[0]
    return 'readfree.com' + url
def parse(s, response):
    tree = etree.HTML(response.text)
    nodes = tree.xpath('//ul[@class="unstyled book-index"]/li')
    for node in nodes:
        item = {}
        item['book_name'] = node.xpath('./div[1]/div[2]/a/text()')[0]
        item['author'] = node.xpath('./div[1]/div[2]/div/a/text()')[0]
        item['DownloadAndPush_num'] = node.xpath('./div/div[3]/text()')
        #down_url = 'https://readfree.com' +  node.xpath('./div[1]/div[2]/a/@href')[0] + '?_pjax=%23pjax'
        #url = parsr_url(s, down_url)
        #item['down_url'] = url
        #将数据存入数据库中
        store_MongoDB(item)
        time.sleep(0.5)
    try:
        next_url = 'https://readfree.com' + tree.xpath('//a[@title="下一页"]/@href')[0]
        response_next = s.get(url=next_url, headers=headers)
        parse(s, response_next)
    except Exception as e:
        print(e)

    


def store_MongoDB(item):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.readfree
    collection = db.books
    collection.insert_one(item)
def main():
    s = requests.Session()
    csrfmiddlewaretoken, captcha_0, captcha_1 = code_download(s)
    #登录
    response = login(s, csrfmiddlewaretoken, captcha_0, captcha_1)

    #解析爬到的数据
    parse(s, response)
    #将数据存入数据库中
 
    #终止
    print("结束")


if __name__ == '__main__':
    main()