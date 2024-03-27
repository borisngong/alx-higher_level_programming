#!/bin/bash
#Bash script that takes in a URL, sends a GET request, and displays response body
curl -sX GET $1 -L