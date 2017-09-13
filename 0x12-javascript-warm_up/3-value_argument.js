#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let argOne = numArgs[0];

if (!argOne) {
  console.log('No argument');
} else {
  console.log(argOne);
}
