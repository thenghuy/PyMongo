from pymongo import MongoClient
import pprint
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
#unset=collection.update_one({"sid":1804220004},{"$unset":{'s_name':""}})
for i in collection.find({"sid":1804220004}):
    pprint.pprint(i)
reset=collection.update_one({"sid":1804220004},{"$set":{'s_name':"Elizabeth"}})
for i in collection.find({"sid":1804220004}):
    pprint.pprint(i)