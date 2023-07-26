from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.kgtljlf.mongodb.net"
client = MongoClient(url)
db = client["pytech"]
col = db["students"]

#return all documents
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x in col.find():
    print("Student ID: " + x["student_id"])
    print("First Name: " + x["first_name"])
    print("Last Name: " + x["last_name"])
    print("\n")

Samantha = {
    "student_id": "1010",
    "first_name": "Samantha",
    "last_name": "Fuller"
}

print("-- INSERT STATEMENTS --")
x = col.insert_one(Samantha)
id = x.inserted_id 
id = str(id)
print("Inserted student record Samantha into students collection with document id" + id)
print("\n")

#return document individually
print("-- DISPLAYING STUDENT TEST DOC")
a = col.find_one({"student_id": "1010"})
print("Student ID: " + a["student_id"])
print("First Name: " + a["first_name"])
print("Last Name: " + a["last_name"])
print("\n")

#delete document
col.delete_one({"student_id": "1010"})

#return all documents
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x in col.find():
    print("Student ID: " + x["student_id"])
    print("First Name: " + x["first_name"])
    print("Last Name: " + x["last_name"])
    print("\n")
