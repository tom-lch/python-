import requests

"""url = 'https://cn.bing.com/ttranslationlookup?&IG=88249127510045B2AD7BFF5CF33DCD4B&IID=translator.5038.7'

formdata = {
    'from': 'en',
    'to': 'zh-CHS',
    'text': 'dog',
}
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
r = requests.post(url, headers= headers, data = formdata)

print(r.json())"""
#使用代理
"""url = 'http://www.baidu.com/s?ie=UTF-8&wd=ip'

proxies = {
    'http' : '121.41.171.223:3128',
}

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

r = requests.get(url, headers = headers, proxies = proxy)

with open('daili.html', 'wb') as fp:
    fp.write(r.content)
"""
"""#使用cookies
#如果碰到会话相关的问题，要首先创建一个会话
#往下所有的操作都通过s操作
s = requests.Session()
post_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201856102257' 
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
formdata = {
    'email':'124235556',
    'icode':'',
    'urigURL':'http://www.renren.com/home',
}
r = s.post(url=post_url, headers=headers, data=formdata)
get_url = 'http://www.renren.com/456474567/profile'
r = s.get(url=get_url)
print(r.content)"""
#chinaunix登录思路：先get 在post 在get
from bs4 import BeautifulSoup
s = requests.Session()
get_url = 'http://bbs.chinaunix.net/member.php?mod=login&action=login&lonsubmit=yes'
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
r = s.get(url=get_url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
formhash = soup.select('input[name="formhash"]')[0]['value']
#向指定的post发送请求
post_url = 'http://bbs.chinaunx.com/adfdvuih&af'
formdata = {
    'formhash':formhash,
    'username':'ffdsfd',
    'pw':'123',
}
res = s.post(url=post_url, headers=headers, data=formdata)

info = 'http:///bbs.chinaunx.com/home.php?adfsdfsrt'
r = s.get(url=info, headers=headers)

 







