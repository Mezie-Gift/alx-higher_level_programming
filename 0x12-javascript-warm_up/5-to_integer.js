#!/usr/bin/node

/* This script prints: `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
  - If the argument cannot be converted to an integer, print `Not a number`.
 */

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else if (process.argv[2]) {
  if (Number.isInteger(process.argv[2]) === true) {
    console.log("My number: ", process.argv[2]);
  } else if (typeof process.argv[2] === 'number' && Number.isInteger(process.argv[2]) !== true) {
    console.log("My number: ", parseInt(process.argv[2]));
  } else {
    if (typeof process.argv[2] === 'string' && isNaN(process.argv[2])) {
      console.log('Not a number');
    } else if (typeof process.argv[2] === 'string' && typeof parseInt(process.argv[2]) === 'number') {
      console.log("My number: ", parseInt(process.argv[2]));
    }
  }
}
