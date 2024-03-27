#!/bin/bash
#Bash script that takes in a URL sends a GET request, and displays response body
curl -s -o /dev/null -w "%{http_code}" "$url" | grep -q 200 && curl -s "$url"