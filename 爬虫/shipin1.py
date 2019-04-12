import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import json
from selenium import webdriver
"""
1、首先向365yg.com发送请求
2、获取响应，解析响应，将里面所有的标题连接获取到
3、依次向每一个标题连接发送请求
4、获取响应，解析响应，获取video标签的src属性
5、向src属性发送请求，获取响应，将北荣保存到本地即可
"""
"""
接口信息：https://www.365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen=1&tadrequire=true&as=A1E57CEA1FCF37E&cp=5CAF1F93C72E8E1&_signature=9j7zlhAXqpsYeKzdiDm5d.Y-84
"""
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
def handle_title(widen):
    #将接口拿过来
    url = 'https://www.365yg.com/api/pc/feed/?min_behot_time=0&category=video_new&utm_source=toutiao&widen={}&tadrequire=true&as=A1E57CEA1FCF37E&cp=5CAF1F93C72E8E1&_signature=9j7zlhAXqpsYeKzdiDm5d.Y-84'
    url = url.format(widen)
    r = requests.get(url=url, headers=headers)
    #解析json,将json数据转化为python对象
    obj  =json.loads(r.text)
    data = obj['data']
    #去除所有与食品相关的数据，data是一个列表，里面放的是字典
    for video_data in data:
        title = video_data['title']
        a_href = video_data['source_url']
        a_href = 'http://365yg.com' + a_href
        #发送请求获取解析内容， 获取src
        handle_href(a_href, title)
    
def handle_href(a_href, title):
    #通过phantomjs来进行解决
    path = r'/Users/samuel/爬虫工具/phantomjs-2.1.1-macosx/bin/phantomjs'
    browser = webdriver.PhantomJS(path)
    browser.get(a_href)
    time.sleep(1)
    #获取元源码
    tree = etree.HTML(browser.page_source)
    video_src = tree.xpath('//video[@mediatype="video"]/source/@src')[0]
    filename = title + '.mp4'
    filepath = 'shipin/' + filename
    r = requests.get(video_src)
    with open(filepath. 'wb') as fp:
        fp.write(r.content)
def main():
    for widen in range(1, 5):
        handle_title(widen)


if __name__ == '__main__':
    main()