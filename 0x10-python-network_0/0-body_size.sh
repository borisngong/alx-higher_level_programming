#!/bin/bash
#A Bash script that takes in a URL, sends a request to that URL, and displays response size
curl -sI $1 | grep "Content-Length" | cut -d " " -f2