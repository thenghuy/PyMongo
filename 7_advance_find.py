from pymongo import MongoClient
import pprint
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
for i in collection.find({"student_id":{"$gt":1804220001}}):
   pprint.pprint(i)
for i in collection.find({"hobbies":{"$in":["Badminton","Cooking","card","videogame"]}}):
  pprint.pprint(i)
