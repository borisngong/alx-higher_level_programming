#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Please provide a URL as an argument."
  exit 1
fi

url="$1"

# Send request and get the size of the response body

body_size=$(curl -sI "$url" | grep -i "content-length" | awk '{print $2}')

# Display the size
echo "$size"
