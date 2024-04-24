#!/usr/bin/node

// Import the native Node.js 'fs' module
const fs = require('fs');

// Import the 'request' module
const request = require('request');

// Utilize the 'request' module to execute an HTTP GET request to the URL
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
