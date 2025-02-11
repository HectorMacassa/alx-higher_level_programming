#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Error: Please provide both URL and file path');
  console.error('Usage: node script.js <url> <file_path>');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching webpage:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', (writeError) => {
    if (writeError) {
      console.error('Error writing to file:', writeError);
      return;
    }
  });
});
