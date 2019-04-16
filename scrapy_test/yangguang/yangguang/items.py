# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    number = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    name = scrapy.Field()
    public_time = scrapy.Field()
    content = scrapy.Field()
    

    

