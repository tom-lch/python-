# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    #职位名
    name = scrapy.Field()
    #链接
    pos_link = scrapy.Field()
    #类别
    pos_Type = scrapy.Field()
    #人数
    pos_nums = scrapy.Field()
    #地点
    pos_loaction = scrapy.Field()
    #发布时间
    pos_time = scrapy.Field()
