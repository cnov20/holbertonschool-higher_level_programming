#!/usr/bin/node

// Script that gets the contents of a webpage and stores them into file
// passed as arguments on command line

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const fileName = process.argv[3];

let fileStream = fs.createWriteStream(fileName);
request(url).pipe(fileStream), function (err, res, body) {
  if (err) {
    console.log(err);
  }
};
