#!/usr/bin/python3
"""
A Python script responsible for taking in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays response body
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})
    response_body = response.text

    print("Response Body:\n", response_body)
