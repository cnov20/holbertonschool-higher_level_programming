#!/usr/bin/node

// Script that writes a string to a file
// passed as arguments on command line

const fs = require('fs');
const file = process.argv[2];
const stringToFile = process.argv[3];

fs.writeFile(file, stringToFile, function (error) {
  if (error) {
    return console.log(error);
  }
});
