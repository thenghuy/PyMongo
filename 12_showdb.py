from pymongo import MongoClient
import pprint
client=MongoClient("mongodb://localhost:27017")
for i in client.list_database_names():
    print(i)