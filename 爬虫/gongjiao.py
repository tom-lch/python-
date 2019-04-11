import requests
import time
from lxml import etree
headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}
#用来保存所有信息
items = []
def parse_navigation():
    url = 'http://zhengzhou.8684.cn/'
    r = requests.get(url, headers = headers)
    #解析内容，获取到黄链接
    tree = etree.HTML(r.text)
    #获取链接
    num_href_list = tree.xpath('//div[@class="bus_kt_r1"]/a/@href')
    return num_href_list

def parse_sanji_route(content):
    tree = etree.HTML(content)
    #依次获取内容
    bus_num = tree.xpath('//div[@class="bus_i_t1"]/h1/text()')[0]
    run_time = tree.xpath('//p[@class="bus_i_t4"][1]/text()')[0]
    ticket_info = tree.xpath('//p[@class="bus_i_t4"][2]/text()')[0]
    #获取更新时间
    gxsj = tree.xpath('//p[@class="bus_i_t4"][4]/text()')[0]
    #获取上行总站数
    total_list = tree.xpath('//span[@class="bus_line_no"]')[0].text
    up_total = total_list[0]
    up_total = up_total.replace('\xa0', '')
    up_site_list = tree.xpath('//div[@class="bus_line_site "][1]/div/div/a/text()')
    try:    
        down_total = total_list[1].replace('\xa0', '')
        down_site_list = tree.xpath('//div[@class="bus_line_site "][2]/div/div/a/text()')
    except Exception as e:
        down_total = []
        down_site_list = []
    #将每一条数据放入字典
    item = {
        '线路名': bus_num,
        '运行时间':run_time,
        '票价信息':ticket_info,
        '更细时间':gxsj,
        '上行站数':up_total,
        '上行站点':up_site_list,
        '下行站数':down_total,
        '下行站点':down_site_list,
    }
    items.append(item)
def parse_ergj_route(content):
    tree = etree.HTML(content)
    #写xpath获取每一条路线列表
    route_list = tree.xpath('//div[@id="con_site_1"]/a/@href')
    for route in route_list:
        route = 'http://zhengzhou.8684.cn/' + route
        r = requests.get(url = route, headers=headers)
        parse_sanji_route(r.text)


def parse_erji(navi_list):
    for url in navi_list:
        url = 'http://zhengzhou.8684.cn/'+url
        r = requests.get(url=url, headers = headers)
        #解析公交路线内容
        parse_ergj_route(r.text)
def main():
    #爬取第一页所有的导航链接
    navi_list = parse_navigation()
    #遍历列表，爬取二级页面每一页的链接，找到所有的公交路线
    parse_erji(navi_list)
    fp = open('郑州公交.txt', 'w', encoding='utf-8')
    for item in items:
        fp.write(str(item)+'\n')
    fp.close()
if __name__ == '__main__':
    main()