#爬取readfree上的数目
#并输出下载量和推量两最多的数的名称
#分别使用re、bs4、xpath进行解析
import urllib.request
import urllib.parse
import re
import http.cookiejar
import time
from bs4 import BeautifulSoup
def parse_content_re(content, book_dict):
    pattren = re.compile(r'<a class="pjax" href="/book/DIY139650/">(.*?)</a>', re.S)
    book_list = pattren.findall(content)
    pattren_1 = re.compile(r'<i class="fa fa-download" title='下载'></i>/d{2}'. re.S)
    book_x_list = pattren.findall(content)
    for key, value in book_list, book_x_list:
        book_dict[key] = value
    return book_dict


def main():
    book_dict = {}
    url = 'https://readfree.me/'
    cj = http.cookiejar.CookieJar()
    handle = urllib.request.HTTPHandler(cj)
    opener = urllib.request.build_opener(handle)
    formdata = {
        'csrfmiddlewaretoken': 'vIYg8WhuEvVlsT1bbwOmr6Tq0GzRu9jt6UjZMQ90uCxHTbkhMUuwBJ4zXtXIevNi',
        'login': '332138569@qq.com',
        'password': 'lichao3335390',
        'captcha_0': '75aa6bd5603ad41ec85ff142551963113359cbbd',
        'captcha_1': 'jvkt',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    reqest = urllib.request.Request(url = url, headers=headers)
    formdata = urllib.parse.urlencode(formdata).encode()
    response = opener.open(reqest, data = formdata)
    #从第一页开始查询知道最后一页
    start_page= int(input('输入开始页码：'))
    end_page= int(input('输入结束页码：'))
    for page in range(start_page, end_page + 1):
        url = url.format(page)
        reqest_page = urllib.request.Request(url = url, headers=headers)
        content = opener.open(reqest_page).read().decode()
        dict = parse_content_re(content, book_dict)
        time.sleep(1)
    return book_dict

if __name__ == '__main__':
    main()