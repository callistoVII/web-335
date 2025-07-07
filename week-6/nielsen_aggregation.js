/**
	Title: nielsen_aggregation.js
    Author: Nicole Nielsen
    Date: 07/06/2025
    Description: Assignment 6.2

 */

// A. Display all students
db.students.find();

// B. Add a new student
db.students.insertOne({
  firstName: "Lily",
  lastName: "Evans",
  studentId: "s1019",
  houseId: "h1007",
});

// Prove the new student was added successfully
db.students.find({
  studentId: "s1019",
});

// C. Update one property of Lily Evans
// This query updates Lily's last name to Potter.
db.students.updateOne({ studentId: "s1019" }, { $set: { lastName: "Potter" } });

// Prove the property was updated
db.students.find({ studentId: "s1019" });

// D. Delete the student we added (sorry Lily)
db.students.deleteOne({ studentId: "s1019" });

// Prove student was removed
db.students.find({ studentId: "s1019" });

// E. Display all students by Hogwarts House
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students",
    },
  },
  {
    $project: {
      _id: 0,
      house: "$houseId",
      students: "$students",
    },
  },
]);

// F. Display all students in Gryffindor
db.houses.aggregate([
  { $match: { houseId: "h1007" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students",
    },
  },
]);

// g. Display all students in the house with an Eagle mascot
db.houses.aggregate([
  { $match: { mascot: "Eagle" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students",
    },
  },
]);
