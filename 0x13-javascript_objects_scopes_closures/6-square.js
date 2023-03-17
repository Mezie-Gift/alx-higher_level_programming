#!/usr/bin/node

/* This module defines a square class that inherits from Square of 5-square.js.
*/
const SquareX = require('./5-square');

class Square extends SquareX {
  /* This defines the square class
  */

  charPrint (c) {
    /* This method prints a square using:
       - the character `c`
       - If c is undefined, it use the character `X`
    */
    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          result += 'X';
        } else {
          result += 'c';
        }
      }
      console.log(result);
    }
  }
}
module.exports = Square;
