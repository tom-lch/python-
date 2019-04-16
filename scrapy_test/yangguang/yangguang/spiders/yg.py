# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr/td/table/tr")
        for tr in tr_list:
            item = YangguangItem()
            item["number"] = tr.xpath("./td[1]/text()").extract_first()
            item["title"] = tr.xpath("./td[2]/a[@class='news14']/text()").extract_first()
            item["href"] = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()
            item["name"] = tr.xpath("./td[4]/text()").extract_first()
            item["public_time"] = tr.xpath("./td[5]/text()").extract_first()
            yield scrapy.Request(
                item["href"],
                callback=self.parse_content,
                meta={"item":item}
                )
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if not next_url:
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_content(self, response):
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='wzy1']/table[2]/td/text()").extract_first()
        print(item)