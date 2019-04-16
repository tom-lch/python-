# -*- coding: utf-8 -*-
import scrapy
from ITcast.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    #爬虫名称 启动爬虫是必须的参数
    name = 'itcast'
    #爬取域范围，允许爬虫在这个域里爬取
    allowed_domains = ['http://www.itcast.cn']
    #爬虫执行后的第一个请求总这里爬取
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml', 'http://www.baidu.com/xxxxxx']
#//div[@class="li_txt"]/h3 姓名
#//div[@class="li_txt"]/h4 职称
#//div[@class="li_txt"]/p 信息
    def parse(self, response):
        node_list = response.xpath('//div[@class="li_txt"]')
        #items = []
        for node in node_list:
            item = ItcastItem()
            item['name'] = node.xpath('./h3/text()').extract_first() #.extract 作用是将xpath对象转换成为text
            item['title'] = node.xpath('./h4/text()').extract_first()
            item['info'] = node.xpath('./p/text()').extract_first()
            #返回给管道
            #return item
            #给引擎继续爬取
            #return scrapy.Request(url)
            #items.append(item)
            #返回数据给管道，之后会继续执行
            yield item
        #return items
