# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#用来处理item
class ItcastPipeline(object):
    def __init__(self):
        self.f = open('iten_pipeline.json', 'w')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False)+'\n'
        self.f.write(content)
        return item

    def close_sipder(self, spider):
        self.f.close()
