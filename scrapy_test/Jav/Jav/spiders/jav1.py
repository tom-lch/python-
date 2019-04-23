# -*- coding: utf-8 -*-
import scrapy
from Jav.items import JavItem

class Jav1Spider(scrapy.Spider):
    name = 'jav1'
    allowed_domains = ['javdb1.com']
    start_urls = ['https://javdb1.com/actors?page=1', 'https://javdb1.com/actors?page=2']
    base_url = 'https://javdb1.com'
    headers = {
        'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    def parse(self, response):
        url_list =response.xpath('//div[@class="box actor-box"]/a/@href').extract()
        for url in url_list:
            url =  self.base_url + url
            yield scrapy.Request(url=url, callback=self.parse_actor, dont_filter=True)

    def parse_actor(self, response):
        url_list =response.xpath('//div[@class="masonry-container"]/div/a/@href').extract()
        for url in url_list:
            url = self.base_url + url
            yield scrapy.Request(url=url, callback=self.parse_meg, dont_filter=True)
            
    
    def parse_meg(self, response):
        item = JavItem()
        item['veido_name'] = response.xpath('//h2[@class="title is-4"]/strong/text()').extract_first()
        item['veido_poster'] = response.xpath('//img[@class="box video-cover"]/@src').extract_first()
        item_list = response.xpath('//span[@class="value"]')
        item['actor_mash'] = item_list[0].xpath('string(.)').extract()[0]
        item['actor_time'] = item_list[1].xpath('string(.)').extract()[0]
        item['vedio_time'] = item_list[2].xpath('./text()').extract_first()
        item['series'] = item_list[6].xpath('string(.)').extract()[0]
        item['vedio_type'] = item_list[7].xpath('string(.)').extract()[0]
        item['actor_name'] = item_list[8].xpath('string(.)').extract()[0]
        try:
            item['magnet'] = response.xpath('//table//a/@href').extract()
        except Exception as e:
            item['magnet'] = [e]
        finally:
            yield item
    
