#!/usr/bin/python3
"""
A Python script responsible for fetching a URL with requests
"""

import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    response_type = type(response.text)
    response_content = response.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(response_type, response_content))
