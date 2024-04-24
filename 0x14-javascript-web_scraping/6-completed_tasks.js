#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

// Perform an HTTP GET request to the specified API URL
request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      // Parse the JSON response into an array of todos
      const todos = JSON.parse(body);

      // Create an object to store the count of completed todos for each userId
      const completed = {};

      // Iterate through each todo
      todos.forEach((todo) => {
        if (todo.completed) {
          // If the todo is completed, increment the count for the corresponding userId
          if (completed[todo.userId] === undefined) {
            completed[todo.userId] = 1;
          } else {
            completed[todo.userId]++;
          }
        }
      });

      // Generate the output based on the completed object
      const output = `{${Object.entries(completed).map(([key, value]) => ` '${key}': ${value}`).join(',\n ')} }`;

      // Output the completed object if it has more than 2 userIds, otherwise output the object itself
      console.log(Object.keys(completed).length > 2 ? output : completed);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
    }
  } else {
    console.error('Error:', error);
  }
});
