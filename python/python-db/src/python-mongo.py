from pymongo import MongoClient
import datetime

mongo=MongoClient(host='localhost',port=27017)
a_document={'name':'jane',
                        'age':34,
                        'interests':['python','database','statistics'],
                        'date_added':datetime.datetime.now()}
# 選擇一個尚未建立的db
db=mongo.my_data
# 選擇一個尚未建立的collection
collection =db.docs
#尋找資料，即使資料庫或資料不存在也不會產生例外異常
collection.find_one()
#列出目前db內所有的collection
print(db.list_collection_names())
collection.insert_one(a_document)
print(db.list_collection_names())
#不設條件尋找一筆資料
print(collection.find_one())
#尋找一筆資料
collection.find_one({'name':'jane'}) 

#MongoDB是用字典(鍵加上值)來進行搜尋以找出文件
#update
collection.update_one({'name':'jane'},{"$set":{'age':29}})
print(collection.find_one())
#replace 替換
collection.replace_one({'name':'jane'},{'username':'flag','date_added':datetime.datetime.now()})
print(collection.find_one())
#delete 刪除
collection.delete_one({'username':'flag'})
print(collection.find_one())
print(db.list_collection_names())
collection.drop()
print(db.list_collection_names())