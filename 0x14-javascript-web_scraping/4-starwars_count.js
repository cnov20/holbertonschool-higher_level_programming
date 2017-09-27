#!/usr/bin/node

// Script that displays the status code of a GET request
// URL passed as argument on command line

const request = require('request');
const url = process.argv[2];
const characterIdUrl = 'https://swapi.co/api/people/18/';

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let json = JSON.parse(body);
    let films = json.results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      let characters = films[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === characterIdUrl) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
