#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  while (list.length) {
    newlist.push(list.pop());
  }
  return (newlist);
};
