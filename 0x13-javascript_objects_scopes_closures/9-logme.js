#!/usr/bin/node

/* This function prints the number of arguments already printed and the new argument value.
 */
exports.logMe = function (item) {
  if (exports.logMe.count > 0) {
    console.log(exports.logMe.count + ': ' + item);
  } else {
    console.log('0: ' + item);
  }
  exports.logMe.count++;
};
exports.logMe.count = 0;
