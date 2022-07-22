from pymongo import MongoClient
import pprint
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
for i in collection.find().sort("student_id",-1):
   pprint.pprint(i)
for i in collection.find().sort("student_id",1):
   pprint.pprint(i)