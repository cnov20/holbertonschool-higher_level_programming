#!/usr/bin/node

// Script that displays the status code of a GET request
// URL passed as argument on command line

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    return (console.log(err));
  }

  let json = JSON.parse(body);
  let obj = {};

  for (let i = 0; i < json.length; i++) {
    let user = json[i].userId;
    obj[user] = 0;
    for (let j = 0; j < json.length; j++) {
      if (json[j].userId === user && json[j].completed) {
        obj[json[i].userId] += 1;
      }
    }
  }
  console.log(obj);
});
