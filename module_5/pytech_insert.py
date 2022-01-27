import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xjcyc.mongodb.net/test"
client = MongoClient(url)
db = client.pytech

guy = {
"first_name" : "Guy",
"last_name" : "Smith",
"student_id" : 1007
}
guy_student_id = db.students.insert_one(guy).inserted_id
print(guy_student_id)

gal = {
"first_name" : "Gal",
"last_name" : "Smith",
"student_id" : 1008
}
gal_student_id = db.students.insert_one(gal).inserted_id
print(gal_student_id)

gus = {
"first_name" : "Gus",
"last_name" : "Smith",
"student_id" : 1009
}
gus_student_id = db.students.insert_one(gus).inserted_id
print(gus_student_id)
