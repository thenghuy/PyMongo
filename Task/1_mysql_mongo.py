import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Keochanny$1",
    database="pytask1"
)
cursor=connection.cursor(dictionary=True)
cursor.execute("SELECT*FROM dse10 where sid=200722003;")
students = cursor.fetchall()

from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017")
db=client["task3"]
collection=db["dse_10_A_student"]
x=collection.insert_many(students)
print("donee")