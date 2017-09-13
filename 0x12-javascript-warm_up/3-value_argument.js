#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);

if (numArgs <= 0) {
  console.log('No argument');
} else {
  console.log(numArgs.toString().split(',').join(' '));
}
