#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
// parseInt numArgs
let num = parseInt(numArgs);
// for i < numArgs.length
//    numArgs[i] = parseInt(numArgs[i])
function sortArgs (num) {
  if (!num || numArgs.length === 1) {
    return (0);
  } else {
    numArgs.sort(function (a, b) {
      return a - b;
    });
    numArgs = numArgs.slice(-2, -1);
    numArgs = parseInt(numArgs);
    return (numArgs);
  }
}
console.log(sortArgs(num));
