/**
	Title: userQuery.js
    Author: Nicole Nielsen
    Date: 06/29/2025
    Description: Assignment 5.2

 */

// a. Add a new user to the collection.
db.users.insertOne({
  firstName: "William",
  lastName: "Adama",
  email: "adama_w@me.com",
  age: 57,
  role: "Battlestar Captain",
});

db.users.insertOne({
  firstName: "Bear",
  lastName: "McCreary",
  email: "bear_mccreary@me.com",
  age: 46,
  role: "Composer",
});

// Prove the new user was added successfully by querying it back
db.users.find({ email: "adama_w@me.com" });

// b. Update Mozart's email address
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

// confirm update was done
db.users.find({ firstName: "Wolfgang" });

// c. Project only first name, last name, and email for all users
db.users.find({}, { _id: 0, firstName: 1, lastName: 1, email: 1 });
