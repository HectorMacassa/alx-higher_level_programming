#!/usr/bin/node

const InitSquare = require('./5-square');

class Square extends InitSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
