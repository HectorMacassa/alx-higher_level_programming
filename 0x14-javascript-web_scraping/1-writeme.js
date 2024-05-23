#!/usr/bin/node

const fs = require('fs');

function writeToFile(filePath, content) {
  try {
    fs.writeFileSync(filePath, content, 'utf8');
  } catch (err) {
    console.error(err);
  }
}

if (process.argv.length < 4) {
  console.error('Please provide a file path and a string as arguments.');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeToFile(filePath, content);
}
