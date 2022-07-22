from pymongo import MongoClient
import pprint
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
for i in collection.find():
    pprint.pprint(i)
#delete=collection.delete_one({'student_id': 1804220001})
print("done")