#!/usr/bin/node
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }
  if (n === 1) {
    return (1);
  }
  return (n * factorial (n - 1));
}
const arg = [];
process.argv.forEach((val, index) => {
  arg[index] = `${val}`;
});
console.log(factorial(arg[2]));
