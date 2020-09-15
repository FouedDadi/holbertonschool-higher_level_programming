#!/usr/bin/node
const i = process.argv[2];
let x;
let y;
if (!isNaN(i)) {
    for (x = 0; x < i; x++) {
        console.log('X'.repeat(i))}
} else { console.log('Missing size'); }
