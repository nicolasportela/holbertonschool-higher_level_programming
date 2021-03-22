#!/usr/bin/node
const number1 = Number(process.argv[2]);
const number2 = Number(process.argv[3]);

function add (a, b) {
  const sum = number1 + number2;
  console.log(sum);
}

add(number1, number2);
