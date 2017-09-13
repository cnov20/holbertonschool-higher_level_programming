#!/usr/bin/node

let args = process.argv;
let numArgs = args.slice(2);

exports.add = function (a, b) {
  a = parseInt(numArgs[0]);
  b = parseInt(numArgs[1]);

  if (numArgs <= 0) {
    console.log(a + b);
  } else {
    console.log(a + b);
  }
};
