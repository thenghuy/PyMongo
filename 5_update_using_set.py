import pprint

from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
update=collection.update_one( {"sid":1507220001},{"$set":{"sid":1804220004}})
print("done")
for i in collection.find({"sid":1804220004}):
    pprint.pprint(i)