#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let words = numArgs.toString().split(',');
let myNum = 'My number: ';

if (numArgs <= 0) {
  console.log(undefined);
} else if (numArgs <= 1) {
  words = undefined;
  console.log(words + 'is undefined');
} else {
  console.log(words.join(' is '));
}
