import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:<password>@cluster0.xjcyc.mongodb.net/test"
client = MongoClient(url)
db = client.pytech

print(db.list_collection_names)