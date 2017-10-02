#!/usr/bin/node

// This script imports an object of occurrences by user id and
// computes another object of user ids by occurrence

const occurenceObject = require('./101-data').dict;

let idsObject = {};
let newKey;

for (let key in occurenceObject) {
  let values = [];

  newKey = occurenceObject[key];
  console.log('New key: ' + newKey);

  for (let key in occurenceObject) {
    if (occurenceObject[key] === newKey) {
      values.push(key);
      console.log('Values:', values);
      delete occurenceObject[key];
    }
  }

  idsObject[newKey] = values;
  console.log(idsObject[newKey]);
}

// Object.entries(occurenceObject).forEach(
//    ([key, value]) => console.log(key, value)
// );

console.log(idsObject);
