#!/usr/bin/node

const request = require('request');

// Utilize the 'request' module to execute an HTTP GET request to the specified URL
request(process.argv[2], function (error, response, body) {
  // Ascertain if no error occurred during the HTTP request.
  if (!error) {
    // Parse the JSON data and retrieve the "results" array
    const results = JSON.parse(body).results;

    // Utilize the 'reduce()' method to iterate through the movies in the 'results' array.
    const moviesWithCharacter18 = results.reduce((count, movie) => {
      // Check if there is a character with ID 18 ('/18/') in the 'characters' array.
      if (movie.characters.find((character) => character.endsWith('/18/'))) {
        // If a character with ID 18 is found, increment the count by 1.
        count++;
      }
      return count;
    }, 0);

    // Log the count of movies with character 18 to the console.
    console.log(moviesWithCharacter18);
  }
});
