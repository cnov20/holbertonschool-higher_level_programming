#!/usr/bin/node

// Script that displays the status code of a GET request
// URL passed as argument on command line

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  console.log('code: ' + res.statusCode);
});
