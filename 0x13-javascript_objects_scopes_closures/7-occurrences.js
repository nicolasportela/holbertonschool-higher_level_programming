#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  const newlist = list.filter(el => el === searchElement);
  for (let i = 0; i < newlist.length; i++) {
    counter = counter + 1;
  }
  return (counter);
};
