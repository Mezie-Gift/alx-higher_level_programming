#!/usr/bin/node

/* This function returns the reversed version of a list.
 */

exports.esrever = function (list) {
  const newList = [];

  for (let i = 1; i <= list.length; i++) {
    if (i === list.length) {
      for (let j = list.length - 1; j >= 0; j--) {
        newList.push(list[j]);
      }
    }
  }
  return newList;
};
