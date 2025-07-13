# Web 335 - Exercise 7.3
# Date: 07/13/2025
# File Name: nielsen_usersp2.py
# Description: Hands on exercise to demonstrate connecting to MongoDB and querying docs using PyMongo, part II

from pymongo import MongoClient
import datetime

# Connect to MongoDB Atlas cluster + access database 
client = MongoClient("mongodb+srv://web355Admin:s3cret@bellevueuniversity.a2hoz8c.mongodb.net/web335DB?retryWrites=true&w=majority")
db = client['BellevueUniversity'] 

# Create user document
niki_user = {
	"firstName": "Niki",
	"lastName": "Nielsen",
	"employeeId": "n2025",
	"email": "nnielsen@example.com",
	"dateCreated": datetime.datetime.utcnow() 
}

# Insert into the collection 

niki_user_id = db.users.insert_one(niki_user).inserted_id
print("Inserted user ID:", niki_user_id)

# Prove the insert worked
print("Inserted Document:", db.users.find_one({"employeeId":"n2025"}))

# Update user's email
db.users.update_one(
	{"employeeId": "n2025"},
	{"$set": {"email": "nik.updated@example.com"}}
)

# Prove the update worked
print("Updated Document", db.users.find_one({"employeeId": "n2025"}))

# Delete the user document
result = db.users.delete_one({ 
	"employeeId": "n2025"
})

# Prove the document was deleted
print(db.users.find_one({"employeeId": "n2025"}))