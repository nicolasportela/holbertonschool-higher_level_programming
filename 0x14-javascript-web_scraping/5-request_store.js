#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request.get(process.argv[2], function (response, body) {
  fs.writeFile(process.argv[3], body.body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
