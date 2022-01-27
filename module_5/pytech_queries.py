import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xjcyc.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

docs = db.students.find({})
 
for doc in docs:
 print(doc)
 
print()

doc = db.students.find_one({'student_id' : 1007})
print(doc)
doc = db.students.find_one({'student_id' : 1008})
print(doc)
doc = db.students.find_one({'student_id' : 1009})
print(doc)