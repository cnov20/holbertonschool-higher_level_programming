#!/usr/bin/node
// Declares and defines a class Rectangle
// via Constructor function with multiple attributes
// With error / specific value handling

module.exports.Rectangle = function Rectangle (w, h) {
  if (!w || !h || w <= 0 || h <= 0) {
    return this;
  }

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
};
