#!/usr/bin/node
exports.esrever = function (list) {
  let longii = list.length - 1;
  let k = 0;
  while (longii - k > 0) {
    const tmp = list[longii];
    list[longii] = list[k];
    list[k] = tmp;
    k++;
    longii--;
  }
  return list;
};
