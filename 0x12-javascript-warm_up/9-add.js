#!/usr/bin/node

/* This script prints the addition of 2 integers
   - The first argument is the first integer
   - The second argument is the second integer
 */

function add (a, b) {
  return a + b;
}
const Num1 = parseInt(process.argv[2]);
const Num2 = parseInt(process.argv[3]);

console.log(add(Num1, Num2));
