#!/usr/bin/node
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function (value) {
  this.value += 1;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
