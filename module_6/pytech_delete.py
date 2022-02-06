import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xjcyc.mongodb.net/test"
client = MongoClient(url)
db = client.pytech

print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")
docs = db.students.find({}, {"_id" : 0})
i = 1
for doc in docs:
    for items in doc.items():
        print(items)       
    print()

gidget = {
"first_name" : "Gidget",
"last_name" : "Smith",
"student_id" : 1010
}

student = gidget
student_id = db.students.insert_one(student).inserted_id
print("-- INSERT STATEMENT --")
student_name_first = student.get("first_name")
student_name_last = student.get("last_name")
pr1 = "Inserted student record " + str(student_name_first) + " " + str(student_name_last)
pr2 = " into the students collection with document_id " + str(student_id)
print(pr1 + pr2)
print()

db.students.delete_one({"student_id": 1010})

print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")
docs = db.students.find({}, {"_id" : 0})
i = 1
for doc in docs:
    for items in doc.items():
        print(items)       
    print()