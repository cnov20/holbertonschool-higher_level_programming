#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let num = parseInt(numArgs);

function sortArgs (num) {
  if (!num || num === 1) {
    return (0);
  } else {
    numArgs = numArgs.sort();
    numArgs = numArgs.slice(-2, -1);
    numArgs = parseInt(numArgs);
    return (numArgs);
  }
}
console.log(sortArgs(numArgs));
