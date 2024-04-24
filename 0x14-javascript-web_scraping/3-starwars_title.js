#!/usr/bin/node

// Import the 'request' module.
const request = require('request');

// Generate the URL for the specific Star Wars film based on the command-line argument.
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

// Make an HTTP GET request to the generated URL using the 'request' module.
request(url, function (error, response, body) {
  // Handle the response: if there is an error, log the error; otherwise, log the film title.
  console.log(error || JSON.parse(body).title);
});
