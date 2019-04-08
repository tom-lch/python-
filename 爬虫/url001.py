import urllib

url = 'http://www.baidu.com'

response = urllib.request.urlopen(url = url)

with opne('baidu.html', 'w', encoding = 'utf-8') as fp:
    fp.write(response.read().decode())