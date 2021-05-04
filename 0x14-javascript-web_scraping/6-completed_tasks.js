#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (err, response, body) {
    if (err) {
	console.log(err);
    }
    let completed = {};
    let tasks = JSON.parse(body);
    for (let i in tasks) {
      let task = tasks[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
});
