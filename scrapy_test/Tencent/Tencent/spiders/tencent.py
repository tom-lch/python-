# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    #爬虫名
    name = 'tencent'
    #爬取域
    allowed_domains = ['tencent.com']
    #start_urls = ['http://hr.tencent.com/']
    #需要拼接的url
    base_url = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    #启动时需要读取的方法
    start_urls = [base_url + str(offset)]
    def parse(self, response):
        #提取的标签列表
        node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        for node in node_list:
            item = TencentItem()
            #提取每个职位的信息
            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['pos_link'] = 'https://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract_first()
            pos_Type = node.xpath('./td[2]/text()').extract_first()
            if not pos_Type:
                item['pos_Type'] = ''
            else:
                item['pos_Type'] = pos_Type
            item['pos_nums'] = node.xpath('./td[3]/text()').extract_first()
            item['pos_loaction'] = node.xpath('./td[4]/text()').extract_first()
            item['pos_time'] = node.xpath('./td[5]/text()').extract_first()
            yield item 
            #第一种写法。拼接url，页面没有连接 只能进行拼接
        """if self.offset < 2190:
            self.offset += 10
            url = self.base_url + str(self.offset)
            yield scrapy.Request(url, callback = self.parse)
        """
        #直接从rsponse里提取连接 直接提取完
        url = response.xpath('//a[@class="noactive" and @id="next"]')
        if not len(url):
            next_url ='https://hr.tencent.com/' + response.xpath('//a[@id="next"]/@href').extract_first()
            #原来是二次解析的域名被过滤掉了，解决办法 1、dont_filter=True 忽略allowed_domains的过滤  2、更换为对应的一级域名
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
    #def parse_next(self, response):





