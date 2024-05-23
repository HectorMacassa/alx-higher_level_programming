#!/usr/bin/node

const request = require('request');
const fs = require('fs');

function getWebpageAndSaveToFile(url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      fs.writeFile(filePath, body, 'utf8', (err) => {
        if (err) {
          console.error(err);
        } else {
          console.log(`Downloaded and saved ${response.headers['content-length']} bytes to ${filePath}`);
        }
      });
    }
  });
}

if (process.argv.length < 4) {
  console.error('Please provide a URL and a file path as arguments.');
} else {
  const url = process.argv[2];
  const filePath = process.argv[3];
  getWebpageAndSaveToFile(url, filePath);
}
