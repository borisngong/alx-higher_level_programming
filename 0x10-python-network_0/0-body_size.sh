#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Please provide a URL as an argument."
  exit 1
fi

# Send request and get the size of the response body
body_size=$(curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2)

# Display the size
echo "$body_size"
