#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);
let  a = parseInt(numArgs[0]);
let  b = parseInt(numArgs[1]);

exports.add = function (a, b) {

  if (numArgs <= 0) {
    console.log(a + b);
  } else {
    console.log(a + b);
  }
};
