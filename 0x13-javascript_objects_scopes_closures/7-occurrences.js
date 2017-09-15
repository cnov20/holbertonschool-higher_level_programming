#!/usr/bin/node
// Function that returns the number of given element in array(list)

module.exports.nbOccurences = function (list, search_element) {
  let occurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === search_element) {
	    occurences += 1;
    }
  }
  return (occurences);
};
