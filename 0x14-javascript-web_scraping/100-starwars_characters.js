#!/usr/bin/node

// Script prints all characters of Star Wars movie

const request = require('request');

const movieId = process.argv[2];
const starWarsFilms = 'http://swapi.co/api/films/';
const film = starWarsFilms + movieId;

request(film, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  let filmBody = JSON.parse(body);
  let characters = filmBody.characters;

  characters.forEach(function (character) {
    request(character, function (err, res, body) {
      if (err) {
        console.log(err);
      }
      let characterInfo = JSON.parse(body);
      console.log(characterInfo.name);
    });
  });
});
