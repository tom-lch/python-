# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuyaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gameFullName = scrapy.Field()
    roomName = scrapy.Field()
    screenshot = scrapy.Field()
    nick = scrapy.Field()
    introduction = scrapy.Field()
