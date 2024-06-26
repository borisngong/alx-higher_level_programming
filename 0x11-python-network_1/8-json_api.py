#!/usr/bin/python3
"""
A Python script responsible for taking in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        json_response = response.json()

        if json_response == {}:
            print("No result")
        else:
            user_id = json_response.get("id")
            user_name = json_response.get("name")
            print("[{}] {}".format(user_id, user_name))

    except ValueError:
        print("Not a valid JSON")
