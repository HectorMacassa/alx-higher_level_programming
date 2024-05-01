#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
    else:
        print("Please provide a URL and an email as command-line arguments.")
        sys.exit(1)

    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    try:
        with urllib.request.urlopen(url, data=data) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.URLError as e:
        print(f"An error occurred: {e.reason}")
