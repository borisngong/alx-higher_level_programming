const fs = require('fs');
// Import the built-in Node.js 'fs' module.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // Write data to a file specified as the third command-line argument (process.argv[2]).
  // Written data is taken from the fourth command-line argument (process.argv[3]).

  if (error) {
    // Handle errors that occur during the write operation.
    console.error('Error occurred while writing the file:', error);
  }
});
