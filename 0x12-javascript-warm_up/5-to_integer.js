#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let words = numArgs.toString().split(',');
let nums = parseInt(words);
let myNum = 'My number: ';

if (numArgs.length === 0 || !nums) {
  console.log('Not a number');
} else {
  console.log(myNum + nums);
}
