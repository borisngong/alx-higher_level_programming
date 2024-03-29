#!/usr/bin/python3
"""
 Python script responsible for taking your GitHub credentials
 and uses the GitHub API to display your id
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    api_url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]

    response = get(api_url, auth=auth.HTTPBasicAuth(username, password))
    json_data = response.json()

    user_id = json_data.get('id')
    print(user_id)
