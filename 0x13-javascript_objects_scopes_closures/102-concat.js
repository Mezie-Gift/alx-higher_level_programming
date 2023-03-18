#!/usr/bin/node

/* This script concats 2 files:
   - The first argument is the file path of the first source file.
   - The second argument is the file path of the second source file.
   - The third argument is the file path of the destination.
 */
const fs = require('fs');
const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
const contents1 = fs.readFileSync(file1, 'utf-8');
const contents2 = fs.readFileSync(file2, 'utf-8');
const combinedContents = contents1 + contents2;
fs.writeFileSync(file3, combinedContents);
