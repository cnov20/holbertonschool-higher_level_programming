#!/usr/bin/node
// Imports Rectangle Object / Class
// Uses this to define Square class which inherits from Rectangle
// Does this via constructor call to parent class

const Rectangle = require('./4-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

module.exports.Square = Square;
