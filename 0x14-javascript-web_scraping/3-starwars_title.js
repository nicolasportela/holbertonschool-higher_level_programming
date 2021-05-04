#!/usr/bin/node
const request = require('request');

request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (response, body) {
  console.log(JSON.parse(body.body).title);
});
