from pymongo import MongoClient
import pprint
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
x=collection.update_many({'batch': 10},{"$set":{ "course":[
                                 {"course_id":"DSE0001","course_name":"DSA","specialization":"programming"},
                                 {"course_id":"DSE0002","course_name":"Pre-calculus1","specialization":"Math"},
                                  {"course_id":"DSE0003","course_name":"Computer science 101","specialization":"programming"}]}})
print(x.modified_count)
for i in collection.find({'batch': 10}):
  pprint.pprint(i)
