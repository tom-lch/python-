from bs4 import BeautifulSoup
from lxml import etree
import re
#使用bs4提取网页信息
soup = BeautifulSoup(open('readfree.me.html'), 'lxml')
lt_list = soup.select('div.book-info a.pjax')
pat = re.compile(r'\w')
pattern = re.compile(r'\d{1,9}')
for lt in lt_list:
    lt = pat.findall(lt.text)
    a = ''
    for i in lt:
        a = i + a
    print(a)
for i in range(20):
    muted_list = soup.select('div.book-meta')[i].text
    lt = pattern.findall(muted_list)
    print(lt)