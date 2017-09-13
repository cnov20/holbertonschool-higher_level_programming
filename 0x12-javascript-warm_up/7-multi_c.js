#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let words = numArgs.toString().split(',');
let nums = parseInt(words);
let myMessage = 'C is fun';

function printMessage () {
  if (!nums) {
    console.log('Missing number of occurences');
  }
  if (numArgs <= 0) {
    return false;
  } else {
    for (let i = 0; i < nums; i++) {
      console.log(myMessage);
    }
  }
}

printMessage();
