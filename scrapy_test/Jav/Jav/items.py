# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    video_name = scrapy.Field()
    video_poster = scrapy.Field()
    actor_mash = scrapy.Field()
    actor_time = scrapy.Field()
    vedio_time = scrapy.Field()
    series = scrapy.Field()
    vedio_type = scrapy.Field()
    actor_name = scrapy.Field()
    magnet = scrapy.Field()


