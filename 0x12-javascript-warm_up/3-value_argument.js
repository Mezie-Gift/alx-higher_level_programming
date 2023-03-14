#!/usr/bin/node

/* This script that prints the first argument passed to it:
   - If no arguments are passed to the script, prints “No argument” */

let firstArg;
process.argv.forEach((value, index) => {
if (index === 2) {
    firstArg = value;
    }
    });
if (firstArg) {
	console.log(firstArg);
} else {
	console.log('No argument');
}

