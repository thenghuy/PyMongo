from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["DSEstudentA1.1"]
record1={
     "student_id":1804220001,
     "student_f_name":"Keo",
     "student_l_name":"Lythenghuy",
     "student_age":17,
     "school":"Kirrirom Institute of Technology",
     "department":"Software engineering",
     "batch":10,
     "adress":{
                       "house_No": "101E0",
                       "street":"44C",
                       "village":"Trea",
                       "district":"Steung Meanchey",
                       "city":"Phnom Penh"
      },
      "hobbies":["Soccer","Movies","Readbook","cycling"]
 }
record2={
     "student_id":1804220002,
     "student_f_name":"Allison",
     "student_l_name":"Ly",
     "student_age":19,
     "school":"Kirrirom Institute of Technology",
     "department":"Software engineering",
     "batch":10,
     "adress":{
                       "house_No": "543",
                       "street":"111",
                       "village":"Silver",
                       "district":"chinatown",
                       "city":"Bangkok"
      },
      "hobbies":["Badminton","Cooking","cycling"]
 }
add=collection.insert_one(record1)
add=collection.insert_one(record2)
collection.drop()
collection=db["dse_10_A_student"]
record1={
     "student_id":1804220001,
     "student_f_name":"Keo",
     "student_l_name":"Lythenghuy",
     "student_age":17,
     "school":"Kirrirom Institute of Technology",
     "department":"Software engineering",
     "batch":10,
     "adress":{
                       "house_No": "101E0",
                       "street":"44C",
                       "village":"Trea",
                       "district":"Steung Meanchey",
                       "city":"Phnom Penh"
      },
      "hobbies":["Soccer","Movies","Readbook","cycling"]
 }
record2={
     "student_id":1804220002,
     "student_f_name":"Allison",
     "student_l_name":"Ly",
     "student_age":19,
     "school":"Kirrirom Institute of Technology",
     "department":"Software engineering",
     "batch":10,
     "adress":{
                       "house_No": "543",
                       "street":"111",
                       "village":"Silver",
                       "district":"chinatown",
                       "city":"Bangkok"
      },
      "hobbies":["Badminton","Cooking","cycling"]
 }
add1=collection.insert_one(record1)
