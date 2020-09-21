#!/usr/bin/node
exports.converter = function (base) {
  return inte => inte.toString(base);
};
