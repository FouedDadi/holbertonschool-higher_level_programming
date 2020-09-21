#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let x = 0;
  let occurence = 0;
  for (x = 0; x < list.length; x++) {
    if (list[x] === searchElement) { occurence = occurence + 1; }
  }
  return occurence;
};
