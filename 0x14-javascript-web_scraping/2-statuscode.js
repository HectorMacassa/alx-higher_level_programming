#!/usr/bin/node

const request = require('request');

function getStatusCode (url) {
  request.get(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}

if (process.argv.length < 3) {
  console.error('Please provide a URL as an argument.');
} else {
  const url = process.argv[2];
  getStatusCode(url);
}
