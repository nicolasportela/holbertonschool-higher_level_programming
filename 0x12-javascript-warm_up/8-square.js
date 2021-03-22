#!/usr/bin/node
const arg = [];
let i;
let str = 'X';
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
const number = Number(`${arg[2]}`);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (i = 0; i < number; i++) {
    console.log(str.repeat(number));
  }
}
