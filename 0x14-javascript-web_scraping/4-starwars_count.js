#!/usr/bin/node

const request = require('request');

function getMovieCount (apiUrl) {
  const wedgeAntillesId = 18;
  const options = {
    url: apiUrl,
    json: true
  };

  request.get(options, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movies = body.results;
      const moviesWithWedge = movies.filter(movie =>
        movie.characters.some(charUrl => charUrl.includes(`${wedgeAntillesId}/`))
      );
      console.log(moviesWithWedge.length);
    }
  });
}

if (process.argv.length < 3) {
  console.error('Please provide the API URL as an argument.');
} else {
  const apiUrl = process.argv[2];
  getMovieCount(apiUrl);
}
