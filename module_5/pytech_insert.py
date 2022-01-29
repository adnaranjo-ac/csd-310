import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xjcyc.mongodb.net/test"
client = MongoClient(url)
db = client.pytech

print("-- INSERT STATEMENTS --")
guy = {
"first_name" : "Guy",
"last_name" : "Smith",
"student_id" : 1007
}

student = guy
student_id = db.students.insert_one(student).inserted_id
student_name_first = student.get("first_name")
student_name_last = student.get("last_name")
pr1 = "Inserted student record " + str(student_name_first) + " " + str(student_name_last)
pr2 = " into the students collection with document_id " + str(student_id)
print(pr1 + pr2)

gal = {
"first_name" : "Gal",
"last_name" : "Smith",
"student_id" : 1008
}

student = gal
student_id = db.students.insert_one(student).inserted_id
student_name_first = student.get("first_name")
student_name_last = student.get("last_name")
pr1 = "Inserted student record " + str(student_name_first) + " " + str(student_name_last)
pr2 = " into the students collection with document_id " + str(student_id)
print(pr1 + pr2)

gus = {
"first_name" : "Gus",
"last_name" : "Smith",
"student_id" : 1009
}

student = gus
student_id = db.students.insert_one(student).inserted_id
student_name_first = student.get("first_name")
student_name_last = student.get("last_name")
pr1 = "Inserted student record " + str(student_name_first) + " " + str(student_name_last)
pr2 = " into the students collection with document_id " + str(student_id)
print(pr1 + pr2)
