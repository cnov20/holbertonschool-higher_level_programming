#!/usr/bin/node

// This script takes in 2 files from the command line as arguments
// And it concatenates them

const fs = require('fs');

const fileOne = process.argv[2];
const fileTwo = process.argv[3];
const fileDestination = process.argv[4];

// console.log(process.argv.length);

if (process.argv.length !== 5) {
  console.log('error');
}

// open destination file for appending
let w = fs.createWriteStream(fileDestination);
// open source file(s) for reading
let r = fs.createReadStream(fileOne);
let r2 = fs.createReadStream(fileTwo);

// w.on('close', function () {
//  console.log('done writing');
// });

r.pipe(w, { end: false });
r2.pipe(w, { end: false });
