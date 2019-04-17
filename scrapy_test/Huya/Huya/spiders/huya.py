# -*- coding: utf-8 -*-
import scrapy
import json
from Huya.items import HuyaItem
class HuyaSpider(scrapy.Spider):
    name = 'huya'
    allowed_domains = ['www.huya.com']
    base_url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2168&tagAll=0&page='
    page = 1
    start_urls = [base_url + str(page)]
    def parse(self, response):
        node_list = json.loads(response.body)["data"]["datas"]
        for node in node_list:
            item = HuyaItem()
            item['gameFullName'] = node['gameFullName']
            item['roomName'] = node['roomName']
            item['screenshot'] = node['screenshot']
            item['nick'] = node['nick']
            item['introduction'] = node['introduction']
            yield item
        self.page += 1
        if self.page <= 9:
            url = self.base_url + str(self.page)
            yield scrapy.Request(url, callback=self.parse)

