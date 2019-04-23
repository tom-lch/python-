# -*- coding: utf-8 -*-
import scrapy
from Jav.items import JavItem

class Jav2Spider(scrapy.Spider):
    name = 'jav2'
    allowed_domains = ['jav1db.com']
    b_url = 'https://javdb1.com/videos?c10=1&page='
    base_url = 'https://javdb1.com'
    page = 1
    start_urls = [b_url + str(page)]

    def parse(self, response):
        url_list =response.xpath('//div[@class="masonry-container"]/div/a/@href').extract()
        for url in url_list:
            url = self.base_url + url
            yield scrapy.Request(url=url, callback=self.parse_meg, dont_filter=True)
        href = response.xpath('//a[@class="pagination-next"]/@href').extract()[0]
        if href == '/videos?c10=1&page=201':
            return 
        next_url =self.base_url + href
        yield scrapy.Request(url=next_url, callback=self.parse, dont_filter=True)

    def parse_meg(self, response):
        item = JavItem()
        item['video_name'] = response.xpath('//h2[@class="title is-4"]/strong/text()').extract_first()
        item['video_poster'] = response.xpath('//img[@class="box video-cover"]/@src').extract_first()
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
    

