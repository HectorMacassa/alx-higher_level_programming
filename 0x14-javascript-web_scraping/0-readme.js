#!/usr/bin/node

const fs = require('fs');

function readFile(filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
}

if (process.argv.length < 3) {
  console.error('Please provide a file path as an argument.');
} else {
  const filePath = process.argv[2];
  readFile(filePath);
}
