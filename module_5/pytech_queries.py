from re import I
import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xjcyc.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print("-- DISPLAYING STUDENT DOCUMENTS FROM find() QUERY --")

docs = db.students.find({}, {"_id" : 0})
i = 1
for doc in docs:
    for items in doc.items():
        print(items)       
    print()

print()
print("DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
doc = db.students.find_one({'student_id' : 1007}, {"_id" : 0})
doc_items = doc.items()
for key, value in doc_items:
    print(key, " : ", value)
print()