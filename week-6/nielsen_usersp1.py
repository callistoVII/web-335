# Web 335 - Exercise 6.3
# Date: 07/06/2025
# File Name: nielsen_usersp1.py
# Description: Hands on exercise to demonstrate connecting to MongoDB and querying docs using PyMongo


from pymongo import MongoClient

# Step 1: Connect to MongoDB Atlas cluster
client = MongoClient("mongodb+srv://web355Admin:s3cret@bellevueuniversity.a2hoz8c.mongodb.net/web335DB?retryWrites=true&w=majority")
db = client['BellevueUniversity']

# Step 2: Display all documents in the user's collection (showing first and last names)
print("\n📋 All users (first and last names):")
for user in db.users.find({}, {"firstName": 1, "lastName": 1}):
    print(user)

# Step 3: Display the document where employeeId is "1011"
print("\n🔍 User with employeeId '1011':")
print(db.users.find_one({"employeeId": "1011"}))

# Step 4: Display the document where lastName is "Mozart"
print("\n🎼 User with lastName 'Mozart':")
print(db.users.find_one({"lastName": "Mozart"}))

