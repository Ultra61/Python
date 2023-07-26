#this way worked better for me then the exact instructions listed
#this returns the ['students'] collection as it should

from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.kgtljlf.mongodb.net"
client = MongoClient(url)
db = client["pytech"]
dblist = client.list_database_names()
if "pytech" in dblist:
    print("database exists!")
print(db.list_collection_names())


