from pymongo import MongoClient

uri = "mongodb://admin:admin@localhost:27017/?authSource=admin"

client = MongoClient(uri)

try:
    print(client.admin.command("ping"))
    print("Connected successfully!")
except Exception as e:
    print(e)