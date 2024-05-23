#!/usr/bin/node

const request = require('request');

function getMovieTitle (episodeId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const data = JSON.parse(body);
      console.log(data.title);
    }
  });
}

if (process.argv.length < 3) {
  console.error('Please provide a movie ID as an argument.');
} else {
  const episodeId = process.argv[2];
  getMovieTitle(episodeId);
}
