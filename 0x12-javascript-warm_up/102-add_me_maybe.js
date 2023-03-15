#!/usr/bin/node

/* This script creates a function that increments and calls a function.
   - Prototype: function (number, theFunction)
 */

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number += 1);
};
