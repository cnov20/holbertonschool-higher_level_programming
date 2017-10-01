#!/usr/bin/node

// This script imports an object of occurrences by user id and
// computes another object of user ids by occurrence

const occurenceObject = require('./101-data').dict;

let idsObject = {};
let array = [];

for (let key in occurenceObject) {
  if (occurenceObject.hasOwnProperty(key)) {
    array = occurenceObject[key];
  }
  idsObject[array] += key;

    // }
}

// Object.entries(occurenceObject).forEach(
//    ([key, value]) => console.log(key, value)
// );

console.log(idsObject);
