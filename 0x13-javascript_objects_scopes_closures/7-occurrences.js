#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const newlist = list.filter(el => el === searchElement);
  for (let i = 0; i < newlist.length; i++) {
    count = count + 1;
  }
  return (cont);
};
