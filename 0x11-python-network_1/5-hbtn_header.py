#!/usr/bin/python3
"""
Responsible for displaying the X-Request-Id header of a request to a given URL
"""
import sys
import requests


if __name__ == "__main__":

    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
