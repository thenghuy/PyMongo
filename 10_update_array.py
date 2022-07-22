from pymongo import MongoClient
import pprint
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
x=collection.update_one({"sid":1804220004},{"$set":{"course.2.course_id":"CS0001"}})
print("done")
for i in collection.find({"sid":1804220004}):
    pprint.pprint(i)