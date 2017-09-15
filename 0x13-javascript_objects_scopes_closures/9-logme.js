#!/usr/bin/node
// Function that prints the num of arguments already printed)
// as well as the new argument value

var current = 0;
module.exports.logMe = function (item) {
  if (item) {
    console.log(current + ': ' + item);
  }
  current += 1;
};
