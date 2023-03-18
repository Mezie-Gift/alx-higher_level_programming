#!/usr/bin/node

/* This function converts a number from base 10 to another base passed as argument.
 */

exports.converter = function (base) {
  return function (baseTenNum) {
    return baseTenNum.toString(base);
  };
};
