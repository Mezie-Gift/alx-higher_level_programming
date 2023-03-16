#!/usr/bin/node

/* This module defines a square class
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  /* This class defines a new square
  */
  constructor (size) {
  /* This method initializes the attributes of the square.
  */
    super(size, size);
  }
}
module.exports = Square;
