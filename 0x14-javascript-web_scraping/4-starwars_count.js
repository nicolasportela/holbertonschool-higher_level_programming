#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (response, body) {
  const results = JSON.parse(body.body).results;
  let count = 0;
  for (const i in results) {
    for (const j in results[i].characters) {
      if (results[i].characters[j].includes('18')) {
        count = count + 1;
      }
    }
  }
  console.log(count);
});
