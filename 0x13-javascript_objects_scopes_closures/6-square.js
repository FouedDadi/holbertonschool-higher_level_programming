#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  charPrint (c) {
    if (c === undefined) { super.print(); } else {
      let x = 0;
      for (x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
