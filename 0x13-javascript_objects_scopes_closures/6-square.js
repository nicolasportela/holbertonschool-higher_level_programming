#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  charPrint (c) {
    let i;
    const str = 'X';
    if (c) {
      for (i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    } else {
      for (i = 0; i < this.width; i++) {
        console.log(str.repeat(this.height));
      }
    }
  }
};
