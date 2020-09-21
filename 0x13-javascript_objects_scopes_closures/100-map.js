#!/usr/bin/node
const lst = require('./100-data.js').list;
console.log(lst);
const map1 = lst.map((x, idx) => (x * idx));
console.log(map1);
