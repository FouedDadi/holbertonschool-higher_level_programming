#!/usr/bin/node
let args = 0;
exports.logMe = function (item) {
  args++;
  console.log((args - 1) + ': ' + item);
};
