#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let words = numArgs.toString().split(',');

if (numArgs <= 0) {
  console.log(undefined + ' is ' + undefined);
} else if (numArgs.length === 1) {
  console.log(words + ' is undefined');
} else {
  console.log(words.join(' is '));
}
