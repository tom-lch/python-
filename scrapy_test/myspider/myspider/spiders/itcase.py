# -*- coding: utf-8 -*-
import scrapy


class ItcaseSpider(scrapy.Spider):
    name = 'itcase'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        #处理start_url地址对应的响应
        #list_ret1 = response.xpath(".//div[@class='tea_con']//h3/text()").extract()
        #print(list_ret1)
        list_ret2 = response.xpath(".//div[@class='tea_con']//li")
        for li in list_ret2 :
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            yield item
