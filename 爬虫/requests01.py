import requests

#url = 'http://www.baidu.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
#r = requests.get(url, headers = headers)
##r.encoding = 'utf-8'
#print(r.text)
#带参数
url = 'https://www.baidu.com/s?wd='
data = {
    'ie':'utf-8',
    'kw':'中国'
}
r = requests.get(url, headers = headers, params=data)
#把结果写到文件中
"""with open('baidu.html', 'wb') as fp:
    fp.write(r.content)"""
print(r.status_code)
print(r.headers)
print(r.url)