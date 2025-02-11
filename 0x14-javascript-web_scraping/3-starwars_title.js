#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Error: Please provide a movie ID');
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  try {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
  }
});
