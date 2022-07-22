from pymongo import MongoClient
import pprint
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
x=collection.update_one({'student_id': 1804220002},{"$set":{"hobbies":["Badminton","Cooking","card","videogame"]}})
for i in collection.find({"hobbies":{"$in":["Badminton","Cooking","card","videogame"]}}):
  pprint.pprint(i)