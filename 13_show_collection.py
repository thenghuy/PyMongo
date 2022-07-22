from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
for i in db.list_collection_names():
    print(i)