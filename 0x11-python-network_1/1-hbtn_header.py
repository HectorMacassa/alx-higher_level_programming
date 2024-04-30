#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = "http://example.com"

    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.getheader("X-Request-Id")
            if request_id:
                print(f"{request_id}")
            else:
                print("X-Request-Id header not found in the response.")
    except urllib.error.URLError as e:
        print(f"An error occurred: {e.reason}")
