#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: Please provide the Star Wars API URL');
  console.error('Usage: node script.js <api_url>');
  process.exit(1);
}

const wedgeId = 18;

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
    const films = JSON.parse(body).results;
    
    const wedgeMovies = films.filter(film => 
      film.characters.some(character => 
        character.includes(`/people/${wedgeId}/`)
      )
    ).length;

    console.log(wedgeMovies);
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
  }
});
