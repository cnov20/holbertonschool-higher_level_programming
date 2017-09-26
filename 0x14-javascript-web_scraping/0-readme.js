#!/usr/bin/node

// Script that reads and prints the content of a file
// passed as argument on command line

let fs = require('fs');
let file = process.argv[2];

fs.readFile(file, 'utf8', function (error, text) {
  if (error) {
      return console.log(error);
  }
  console.log(text);
});
