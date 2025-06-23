/**
	Title: userQuery.js
    Author: Nicole Nielsen
    Date: 06/22/2025
    Description: MongoDB Shell Scripts for the users collection.
 */

// a. Display all users in the collection
print("All users:");
db.users.find().forEach((doc) => printjson(doc));

// b. Display the user with the email address jbach@me.com
print("\nUser with email 'jbach@me.com':");
printjson(db.users.findOne({ email: "jbach@me.com" }));

// c. Display the user with the last name Mozart
print("\nUser with last name 'Mozart':");
printjson(db.users.findOne({ lastName: "Mozart" }));

// d. Display the user with the first name Richard
print("\nUser with first name 'Richard':");
printjson(db.users.findOne({ firstName: "Richard" }));

// e. Display the user with employeeId 1010
print("\nUser with employeeId 1010:");
printjson(db.users.findOne({ employeeId: 1010 }));
