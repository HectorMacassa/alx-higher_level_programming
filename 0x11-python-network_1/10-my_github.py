#!/usr/bin/python3
"""
A Python script that takes GitHub credentials (username and password) and
uses the GitHub API to display id
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_info = response.json()
        print(user_info.get("id"))
    else:
        print("None")
