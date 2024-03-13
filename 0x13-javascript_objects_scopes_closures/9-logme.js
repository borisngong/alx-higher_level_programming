#!/usr/bin/node
let arg_num = 0;

exports.logMe = function (item) {
  console.log(arg_num + ': ' + item);
  arg_num++;
};
