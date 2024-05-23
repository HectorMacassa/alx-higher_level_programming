#!/usr/bin/node

const request = require('request');

function getCompletedTasks(apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const tasks = JSON.parse(body);
      const userTasks = tasks.reduce((acc, task) => {
        const { userId, completed } = task;
        if (completed) {
          acc[userId] = acc[userId] ? acc[userId] + 1 : 1;
        }
        return acc;
      }, {});

      for (const userId in userTasks) {
        console.log(`${userId}: ${userTasks[userId]}`);
      }
    }
  });
}

if (process.argv.length < 3) {
  console.error('Please provide the API URL as an argument.');
} else {
  const apiUrl = process.argv[2];
  getCompletedTasks(apiUrl);
}
