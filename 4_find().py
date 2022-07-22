from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
import pprint
thing_need_to_Find=int(input("Enter here:"))
for i in collection.find({"student_id":thing_need_to_Find}):
 pprint.pprint(i)
for i in collection.find():
    pprint.pprint(i)