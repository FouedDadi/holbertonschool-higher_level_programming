#!/usr/bin/node
let list = process.argv;
if (list.length > 3) {
  list = list.sort((a, b) => a - b);
  list = list.reverse();
  console.log(list[1]);
} else {
  console.log(0);
}
