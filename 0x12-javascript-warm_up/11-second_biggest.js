#!/usr/bin/node
const listarg = [];
let max;
let max2;
process.argv.forEach((val, index) => {
  listarg[index] = `${val}`;
});
if (listarg.length <= 3) {
  console.log('0');
} else {
  for (let i = 0; i <= listarg.length; i++) {
    if (listarg[i] > listarg[i - 1]) {
      max2 = max;
      max = listarg[i];
    } else {
      continue;
    }
  }
  console.log(max2);
}
