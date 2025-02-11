#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || content === undefined) {
  console.error('Error: Please provide both file path and string to write');
  console.error('Usage: node script.js <file_path> <string_to_write>');
  process.exit(1);
}

fs.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    // Print error object if writing fails
    console.error(error);
    return;
  }
});
