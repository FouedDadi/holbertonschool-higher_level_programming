#!/usr/bin/node
let list = process.argv;
if (list.length > 2) {
  list = list.sort();
  list = list.reverse();
  console.log(list[1]);
} else {
  console.log(0);
}
