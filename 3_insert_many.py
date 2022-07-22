from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
record=[{
     "student_id":1804220003,
     "student_f_name":"Daniel",
     "student_l_name":"Ou",
     "student_age":18,
     "school":"Kirrirom Institute of Technology",
     "department":"Software engineering",
     "batch":10,
     "adress":{
                       "house_No": "101E2",
                       "street":"11",
                       "village":"99",
                       "district":"Bandan",
                       "city":"Buriram"
      },
      "hobbies":["Basketball","Reading","Hanging out"]
 },




{
     "sid":1507220001,
     "s_name":"Lythenghuykeo",
     "course":[
                                 {"course_id":"DSE0001","course_name":"DSA","specialization":"programming"},
                                 {"course_id":"DSE0002","course_name":"Pre-calculus1","specialization":"Math"},
                                  {"course_id":"DSE0003","course_name":"Computer science 101","specialization":"programming"}
     ]
}]
add=collection.insert_many(record)