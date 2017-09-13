#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let num = parseInt(numArgs[0]);

function factorial (num) {
  if (num < 0) {
    return (-1);
  } else if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

console.log(factorial(num));
