import pymongo
# todo:用于基于'_id'查询
from bson.objectid import ObjectId

# 1、创建mongodb的链接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# client=pymongo.MongoClient('mongodb://localhost:27017/')

# 2、指定数据库
#db = client.test
#db = client.movies
#db = client.taobao
#db = client.quotestutorial
#db = client.yangguang
db = client.sunning

# 3、创建collection对象,类似于关系型中的表
#collection = db.students
#collection = db.movies
#collection = db.QuoteItem
#collection = db.YangguangItem
collection = db.SunningItem

# # 插入单条数据
# student = {
#     'id': '20147206',
#     'name':'ch',
#     'age':24,
#     'gender':'male'
# }
# result=collection.insert_one(student1)
# print(result)
# print(result.inserted_ids)


# student1 = {
#     'id': '20147206',
#     'name':'ch',
#     'age':24,
#     'gender':'male'
# }
# student2 = {
#     'id': '20147207',
#     'name':'zt',
#     'age':24,
#     'gender':'male'
# }
# result=collection.insert_many([student1,student2])
# print(result)
# print(result.inserted_ids)

# 查询
# results = collection.find({'age': 24})
# print(type(results))
# for result in results:
#     print(result)

# # 单查询
# result = collection.find_one({'_id': ObjectId('5e8a82a120672b8328febb4b')})
# print(result)

# #计数
# count=collection.find().count()
# print(count)

#result=collection.drop()
results=collection.find()
for result in results:
    print(result)

