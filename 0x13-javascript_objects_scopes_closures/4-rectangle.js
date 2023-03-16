#!/usr/bin/node

/* This module Rectangle defines a rectangle
 */

class Rectangle {
  /* This class defines a rectangle
   */

  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /* This method prints a rectangle using `X`
     */
    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) {
        result += 'X';
      }
      console.log(result);
    }
  }

  rotate () {
    /* This method swaps the value of with and height.
    */
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
    return [this.width, this.height];
  }

  double () {
    /* This method doubles the value of height and width.
    */
    this.width *= 2;
    this.height *= 2;
    return [this.width, this.height];
  }
}
module.exports = Rectangle;
