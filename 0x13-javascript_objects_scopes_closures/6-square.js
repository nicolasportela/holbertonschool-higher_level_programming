#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    let i;
    if (c === undefined) {
      this.print();
    } else {
      for (i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};