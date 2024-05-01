#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if isinstance(data, list):
            for user in data:
                print("[{}] {}".format(user.get("id"), user.get("name")))
        elif isinstance(data, dict):
            print("[{}] {}".format(data.get("id"), data.get("name")))
        elif data:
            print(data)
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
