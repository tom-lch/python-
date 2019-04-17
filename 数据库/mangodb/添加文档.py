from pymongo import MongoClient
from bson.objectid import ObjectId  #ID查询必须导入的库
conn = MongoClient("localhost", 27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

collection.insert({'name':"tom", 'age':18, 'gender':1, 'address':"北京", 'isDelete':0})

#查询文档
"""collection.find()"""
#查询部分文档
"""res = collection.find('age':{'$gt':18})
for row in res:
    print(row)
    print(type(row))"""

res1 = collection.find('age':{'$gt':18}).count()
#根据id查询
res2 = collection.find({'_id':ObjectId(34534645645645)})

#排序
re3 = collection.fiind().sort("age", pymongo.DESCENDING)

res4 = collection.find().skip(2), limit(2)
#更新
ret5 = collection.update({'name':"lili"}, {"$set":{"age":25}})
#删除
collection.remove()
#删除
conn.close()