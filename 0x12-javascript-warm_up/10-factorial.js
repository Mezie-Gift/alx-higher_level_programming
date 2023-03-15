#!/usr/bin/node

/* This script computes and prints a factorial.
   - The first argument is an integer (argument can be cast as an integer)
   - Factorial of NaN is 1
   - It is done recursively
   - A function must be used
 */

function fact (n) {
  if (isNaN(n)) {
    return 1;
  } else {
    if (n === 0 || n === 1) {
      return 1;
    } else {
      return n * fact(n - 1);
    }
  }
}
const Num = parseInt(process.argv[2]);
console.log(fact(Num));
