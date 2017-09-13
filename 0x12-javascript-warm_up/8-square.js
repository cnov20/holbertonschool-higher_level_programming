#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let words = numArgs.toString().split(',');
let nums = parseInt(words);
let squareRep = 'X';

function printSquare (nums) {
  if (!nums) {
    console.log('Missing size');
  }
  if (numArgs <= 0) {
    return false;
  } else {
    for (let i = 0; i < nums; i++) {
      for (let j = 0; j < nums; j++) {
        console.log(squareRep);
      }
    }
  }
}

printSquare(nums);
