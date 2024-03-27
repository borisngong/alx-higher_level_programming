#!/bin/bash
#Bash script that takes in a URL sends a GET request, and displays response body
curl -sfL "$1" -X GET