#!/usr/bin/python3
"""
A Python script Responsible for taking in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the header of
the response
"""
import urllib.request
import sys

first_command_arg = sys.argv[1]

if __name__ == "__main__":
    with urllib.request.urlopen(first_command_arg) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
