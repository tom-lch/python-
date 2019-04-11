import requests
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request
#解决验证码问题
#  手动输入
#  tesseract 简介
#  打码平台
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
def download_code(s):
    url = 'https://readfree.me/auth/login/?next=/'
    r = s.get(url=url, headers=headers)
    tree = etree.HTML(r.text)
    #得到图片链接
    image_src = 'https://readfree.me' + tree.xpath('//img[@class="captcha"]/@src')[0]
    #将验证码图片下载到本地
    """
    t_image = s.get(image_src, headers=headers)
    with open('code.png', 'wb') as fp:
        fp.write(t_image.content)
    """
    urllib.request.urlretrieve(image_src, 'code.png')
    #解析表单
    csrf_value = tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')[0]
    captcha_0 = tree.xpath('//input[@id="id_captcha_0"]/@value')[0]
    return csrf_value, captcha_0
def login(s, csrf_value, captcha_0):    
    post_url = 'https://readfree.me/auth/login/?next=/'
    #提示用户输入验证码
    code = input("输入验证码：")
    formdata = {
        'csrfmiddlewaretoken':csrf_value,
        'login':'332138569@qq.com',
        'password':'lichao3335390',
        'captcha_0':captcha_0,
        'captcha_1':code,
    }
    r = s.post(url = post_url, headers=headers, data = formdata)
    print(r.text)
def main():
    #下载验证码到本地
    s = requests.Session()
    csrf_value, captcha_0 = download_code(s)
    #登录 向post地址发送请求
    login(s,csrf_value, captcha_0)


if __name__=='__main__':
    main()