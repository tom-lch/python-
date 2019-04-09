import urllib.request
import urllib.parse
from lxml import etree
import os
import time
#描述：爬取妹子图
def handle_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    request = urllib.request.Request(url = url, headers=headers)
    return request
#解析网页中的每一张图片的连接 并返回链接
def parse_content(content):
    lt = etree.HTML(content)
    url_image_list = lt.xpath('//li/a[@target="_blank"]/@href')
    return url_image_list

def parse_image(content):
    lt = etree.HTML(content)
    image_src = lt.xpath('//div[@class="main-image"]//img/@src')
    return image_src

def storage(src):
    dirname = 'mzitu'
    if  not os.path.exists(dirname):
        os.mkdir(dirname)
    #urllib.request.urlretrieve(src)
    filename = src.split('/')[-1]
    filepath = dirname + '/' + filename
    print('%s图片正在下载。。。' % filename)
    #此处有防盗链无法下载
    urllib.request.urlretrieve(src, filepath)
    print(src)
    print('%s图片结束下载。。。' % filename)

def main():
    #url起始地址
    url = 'https://www.mzitu.com/xinggan/page/{}/'
    start_page = int(input("输入开始页码："))
    end_page = int(input("输入结束页码："))
    for page in range(start_page, end_page + 1):
        url = url.format(page)
        request = handle_request(url)
        #获取网页的内容
        content = urllib.request.urlopen(request).read().decode()
        #解析网页
        url_image_list = parse_content(content)
        #遍历每一个图片的链接获取图片集
        for image_url in url_image_list:
            image_request = handle_request(image_url)
            image_content = urllib.request.urlopen(image_request).read().decode()
            src = parse_image(image_content)[0]
            #存储图片
            storage(src)
        time.sleep(1)



if __name__ == '__main__':
    main()