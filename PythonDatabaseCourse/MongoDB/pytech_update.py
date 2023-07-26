from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.kgtljlf.mongodb.net"
client = MongoClient(url)
db = client["pytech"]
col = db["students"]
#make sure database exists
"""
dblist = client.list_database_names()
if "pytech" in dblist:
    print("database exists!")
#make sure collection exists
collist = db.list_collection_names()
if "students" in collist:
    print("collection exists!")
"""
#return all documents
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x in col.find():
    print("Student ID: " + x["student_id"])
    print("First Name: " + x["first_name"])
    print("Last Name: " + x["last_name"])
    print("\n")

#update student record
col.update_one({"student_id": "1007"},
                {"$set":{"last_name":"Meyer"}})

#return document individually
print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
a = col.find_one({"student_id": "1007"})
print("Student ID: " + a["student_id"])
print("First Name: " + a["first_name"])
print("Last Name: " + a["last_name"])

client.close()