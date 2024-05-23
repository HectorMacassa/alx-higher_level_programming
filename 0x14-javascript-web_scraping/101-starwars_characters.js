#!/usr/bin/node

const request = require('request');

function getMovieCharacters(movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;

      const getCharacters = () => {
        if (characterUrls.length === 0) {
          return;
        }

        const characterUrl = characterUrls.shift();

        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            const character = JSON.parse(body);
            console.log(character.name);
            getCharacters();
          }
        });
      };

      getCharacters();
    }
  });
}

if (process.argv.length < 3) {
  console.error('Please provide a movie ID as an argument.');
} else {
  const movieId = process.argv[2];
  getMovieCharacters(movieId);
}
