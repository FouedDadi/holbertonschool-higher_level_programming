#!/usr/bin/node
const str = 'C is fun';
const i = process.argv[2];
let x;
if (!isNaN(i)) {
  for (x = 0; x < i; x++) { console.log(str); }
} else { console.log('Missing number of occurrences'); }
