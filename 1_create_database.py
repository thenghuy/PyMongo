from pymongo import MongoClient
client=MongoClient('localhost',27017)
db=client["task3"]
print("DB created")