#!/usr/bin/python3
"""
A Python script responsible for taking in a URL, sends a request to the URL
and displays the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    status_code = response.status_code

    if status_code >= 400:
        print("Error code: {}".format(status_code))
    else:
        response_body = response.text
        print(response_body)
