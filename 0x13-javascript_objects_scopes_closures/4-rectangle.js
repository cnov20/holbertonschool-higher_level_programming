#!/usr/bin/node
// Declares and defines a class Rectangle
// via Constructor function with multiple attributes
// With error / specific value handling
// print() instance method to display representation of object
// rotate() instance method that exchanges object width and height
// double() instance method that multiplies width and height of obj by 2

module.exports.Rectangle = function Rectangle (w, h) {
  if (!w || !h || w <= 0 || h <= 0) { return this; }

  this.width = w;
  this.height = h;

  this.print = function () {
    let rectangleRep = '';
    for (let i = 0; i < this.width; i++) {
      rectangleRep += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(rectangleRep);
    }
  };

  this.rotate = function () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  };

  this.double = function () {
    this.width *= 2;
    this.height *= 2;
  };
};
