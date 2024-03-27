#!/bin/bash
#Bash script that takes in a URL, sends a GET request, and displays response body
if [ $(curl -L -s -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -Ls "$1"; fi