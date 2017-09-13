#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let size = parseInt(numArgs);
let squareRep = '';

function printSquare (size) {
  if (!size) {
    console.log('Missing size');
  } else if (size.length < 0) {
    return false;
  } else {
    for (let i = 0; i < size; i++) {
      squareRep += 'X';
    }
    for (let j = 0; j < size; j++) {
      console.log(squareRep);
    }
  }
}

printSquare(size);
