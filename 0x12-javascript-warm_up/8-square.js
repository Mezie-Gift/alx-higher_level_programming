#!/usr/bin/node

/* This script prints a square
   - The first argument is the size of the square.
   - If the first argument can’t be converted to an integer, print “Missing size”.
   - The character X is used to print the square.
 */

const size = parseInt(process.argv[2]);

if (isNaN(size) || typeof size === 'string') {
  console.log('Missing size');
} for (let height = 0; height < size; height++) {
  let result = '';
  for (let width = 0; width < size; width++) {
    result += 'X';
  }
  console.log(result);
}
