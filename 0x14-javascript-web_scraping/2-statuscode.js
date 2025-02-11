#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Error: Please provide a URL');
  console.error('Usage: node script.js <url>');
  process.exit(1);
}

request.get(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  
  console.log(`code: ${response.statusCode}`);
});
