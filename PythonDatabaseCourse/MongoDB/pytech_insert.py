#in the previous assignment I submitted on Bellevue's website there are some comments saying the program does not work, it does work those are wrong
#GitHub has the updated file which is the same with those comments removed
from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.kgtljlf.mongodb.net"
client = MongoClient(url)
db = client["pytech"]
col = db["students"]
#make sure database exists
dblist = client.list_database_names()
if "pytech" in dblist:
    print("database exists!")
#make sure collection exists
collist = db.list_collection_names()
if "students" in collist:
    print("collection exists!")

#documents
Jake = {
    "student_id": "1007",
    "first_name": "Jake",
    "last_name": "Witherspoon"
}

Lisa = {
    "student_id": "1008",
    "first_name": "Lisa",
    "last_name": "Jefferson"
}

Trevor = {
    "student_id": "1009",
    "first_name": "Trevor",
    "last_name": "Potts"
}

#add documents to database and print the IDs
x = col.insert_one(Jake)
id = x.inserted_id 
id = str(id)
print("Inserted student record Jake into students collection with document id" + id)

x = col.insert_one(Lisa)
id = x.inserted_id
id = str(id)
print("Inserted student record Lisa into students collection with document id" + id)

x = col.insert_one(Trevor)
id = x.inserted_id
id = str(id)
print("Inserted student record Trevor into students collection with document id" + id)

