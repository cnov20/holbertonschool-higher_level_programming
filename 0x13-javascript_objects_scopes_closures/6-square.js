#!/usr/bin/node
// Imports Rectangle Object / Class
// Uses this to define Square class which inherits from Rectangle
// Does this via constructor call to parent class
// Adds printChar() method to Square.prototype object
const Square = require('./5-square').Square;

Square.prototype.charPrint = function (c) {
  if (!c) { c = 'X'; }

  for (let i = 0; i < this.height; i++) {
    for (let j = 0; j < this.width; j++) {
      process.stdout.write(c);
    }
    console.log();
  }
};

module.exports.Square = Square;
