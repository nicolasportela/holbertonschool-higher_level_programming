#!/usr/bin/node
const listarg = [];
process.argv.forEach((val, index) => {
  listarg[index] = `${val}`;
});
if (listarg.length <= 3) {
  console.log('0');
} else {
  listarg.sort(function (a, b) { return a - b; });
  console.log(listarg[listarg.length - 2]);
}
