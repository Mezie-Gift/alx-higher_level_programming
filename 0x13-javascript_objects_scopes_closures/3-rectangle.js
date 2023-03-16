#!/usr/bin/node
/* Module defines a Rectangle class
 */

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
  /* prints a rectangle using `X`
     */

    for (let i = 0; i < this.height; i++) {
      let result = '';
      for (let j = 0; j < this.width; j++) {
        result += 'X';
      }
      console.log(result);
    }
  }
}
module.exports = Rectangle;
