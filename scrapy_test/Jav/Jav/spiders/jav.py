# -*- coding: utf-8 -*-
import scrapy
from Jav.items import JavItem
import requests
from lxml import etree
#此版本有bug
class JavSpider(scrapy.Spider):
    name = 'jav'
    allowed_domains = ['javdb1.com']
    start_urls = ['https://javdb1.com/actors?page=1']
    base_url = 'https://javdb1.com'
    headers = {
        'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    def parse(self, response):
        #解析出每一个女优的单个情况
        node_list = response.xpath('//div[@class="box actor-box"]')
        for node in node_list:
            item = JavItem()
            item['actor_name'] = node.xpath('./a/@title').extract_first()
            item['actor_img'] = node.xpath('./a/figure/img/@src').extract_first()
            url = self.base_url + node.xpath('./a/@href').extract_first()
            #yield scrapy.Request(url=url, callback=lambda responsem it=item: self.parse_actor(response, it), dont_filter=True)
            #item['move_list'] = self.parse_actor(url)
        yield item
    def parse_actor(self, response, it):
        video_list = response.xpath('//div[@id="videos"]/div/div')
        actor_video_list = []
        for video in video_list:
            dict_video = {}
            dict_video['mash'] = video[0].text_content().xpath['./a/div[@class="uid"]/text()'][0]
            dict_video['name'] = video[0].text_content().xpath['./a/h3/text()/text()'][0]
            dict_video['img'] = video[0].text_content().xpath['./a/div[@class="brick-image"]/img/@src'][0]
            url = self.base_url + video[0].text_content().xpath['./a/@href'][0]
            #dict_video['magnet'] = scrapy.Request(url=url, callback=self.av_video_parse_link, dont_filter=True)
            dict_video['magnet'] = self.av_video_parse_link(url)
            actor_video_list.append(dict_video)
            print(actor_video_list)
        return actor_video_list

    def av_video_parse_link(self, url):
        response = requests.get(url=url, headers=self.headers)
        tree = etree.HTML(response.text)
        table = tree.xpath('div[@class="message-body"]/table')
        magnet = []
        if table:
            magnet = []
        else:
            magnet = table.xpath('//td[@class="magnet-name"]/a/@href')
        print(magnet)
        return magnet
