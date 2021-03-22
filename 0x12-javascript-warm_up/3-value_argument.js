#!/usr/bin/node
const arg = [];
let ind;
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
  ind = `${index}`;
});
if (ind < 2) {
  console.log('No argument');
} else {
  console.log(arg[2]);
}
