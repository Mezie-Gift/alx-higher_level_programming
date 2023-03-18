#!/usr/bin/node

/* This script imports an array and computes a new array using the map().
 */

const list = require('./100-data').list;
console.log(list);
console.log(list.map((x, i) => x * i));
