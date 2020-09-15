#!/usr/bin/node
function fact (num) {
  if (num === 0) { return 1; } else if (isNaN(num)) { return 1; } else {
    return (num * fact(num - 1));
  }
}
console.log(fact(process.argv[2]));
