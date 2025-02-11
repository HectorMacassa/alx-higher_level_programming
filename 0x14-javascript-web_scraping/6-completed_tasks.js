#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: Please provide the API URL');
  console.error('Usage: node script.js <api_url>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }

  try {
    const todos = JSON.parse(body);
    
    const completedTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        completedTasks[todo.userId] = (completedTasks[todo.userId] || 0) + 1;
      }
    });

    console.log(completedTasks);
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
  }
});
