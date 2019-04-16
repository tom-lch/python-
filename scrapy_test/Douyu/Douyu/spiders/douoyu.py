# -*- coding: utf-8 -*-
import scrapy


class DouoyuSpider(scrapy.Spider):
    name = 'douoyu'
    allowed_domains = ['douyucdn.cn']
    start_urls = ['http://douyucdn.cn/']

    def parse(self, response):
        pass
