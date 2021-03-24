#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cont = 0;
  const newlist = list.filter(el => el === searchElement);
  for (let i = 0; i < newlist.length; i++) {
    cont = cont + 1;
  }
  return (cont);
};
