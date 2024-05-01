#!/usr/bin/python3

"""
Takes in a URL, sends a request to the URL and displays the body of theresponse
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"An error occurred: {e.reason}")
