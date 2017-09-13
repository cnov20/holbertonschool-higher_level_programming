#!/usr/bin/node

exports.add = function (a, b) {
  if (!a || !b) {
    return false;
  } else {
    return a + b;
  }
};
