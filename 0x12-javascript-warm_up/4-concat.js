#!/usr/bin/node

/* This script prints two arguments passed to it, in the following format:<arg1> “ is ” <arg2>
 */

if (process.argv.length < 3) {
  console.log('undefined' + ' is ' + 'undefined');
} else if (process.argv.length >= 2) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
