#!/usr/bin/node

/* This script searches the second biggest integer in the list of arguments.
   - You can assume all arguments can be converted to integer
   - If 1 OR 0 argument passed, print 0.
 */

const args = process.argv.slice(2).map(Number); // convert command line arguments to an array of integers
const argsLength = args.length;

if (argsLength === 0) {
console.log(0);
} else if (argsLength === 1) {
console.log(0);
} else {
let largest = -Infinity;
let secondLargest = -Infinity;
for (let i = 0; i < argsLength; i++) {
const current = args[i];
if (current > largest) {
secondLargest = largest;
largest = current;
} else if (current > secondLargest && current !== largest) {
secondLargest = current;
}
}
console.log(secondLargest);
}
