#!/usr/bin/node

// Function that converts a number from base 10
// to another base passed as argument

module.exports.converter = function (base) {
  return function decToBase (num) {
    if (base) {
      return (num.toString(base));
    }
  };
};
