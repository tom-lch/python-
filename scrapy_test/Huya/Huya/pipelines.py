# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
"""
#class HuyaPipeline(object):
    def __init__(self):
        self.f = open('huya.json', 'w')
    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False) + ',\n')
        return item
    def close_scrapy(self):
        self.f.close()
    def __init__(self):
        host = Mongoip
        port = MongoPort
        dbName = MongoDBname
        client = MongoClient(host=host, port=port)
        db = client[dbName]
        self.post = db[MongoItem]
    def process_item(self, item, spider):
        huya_yanzhi = dict(item)
        self.post.insert(huya_yanzhi)
        return item
"""
class MongoPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(dict(item))
        return item

