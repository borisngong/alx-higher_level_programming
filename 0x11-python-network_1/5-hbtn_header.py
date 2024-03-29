#!/usr/bin/python3
"""
Responsible for displaying the X-Request-Id header of a request to a given URL
"""
import sys, requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
