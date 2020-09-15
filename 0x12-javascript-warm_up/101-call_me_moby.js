#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  for (let y = 0; y < x; y++) { func(); }
};
