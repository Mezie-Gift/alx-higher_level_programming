#!/usr/bin/node

/* This script prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
   - The first line: “C is fun”
   - The second line: “Python is cool”
   - The third line: “JavaScript is amazing”
 */

const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i < myArray.length; i++) {
  console.log(myArray[i]);
}
