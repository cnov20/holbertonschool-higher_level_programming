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
    for (let i = 0; i < w; i++) {
	    rectangleRep += 'X';
    }
    for (let j = 0; j < h; j++) {
	    console.log(rectangleRep);
    }
  };

  this.double = function () {
    w *= 2;
    h *= 2;
  };

  this.rotate = function () {
    temp = w;
    w = h;
    h = temp;
  };
};
