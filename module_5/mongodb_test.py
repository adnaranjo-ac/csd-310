import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.xjcyc.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print("--Collections--")
print(db.list_collection_names())