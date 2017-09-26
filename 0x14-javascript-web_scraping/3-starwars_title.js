#!/usr/bin/node

// Script that displays the status code of a GET request
// URL passed as argument on command line

const request = require('request');
const episodeId = process.argv[2];
const url = 'http://swapi.co/api/films/' + episodeId;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let json = JSON.parse(body);
  console.log(json.title);
});
