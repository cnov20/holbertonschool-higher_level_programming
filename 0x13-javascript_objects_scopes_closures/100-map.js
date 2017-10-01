#!/usr/bin/node

// This script imports an array and computes a new array
// Utilizing the map built-in function

const array = require('./100-data').list;

let newArray = array.map(function (currentValue, index, array) {
  return (currentValue * index);
});

console.log(array);
console.log(newArray);
