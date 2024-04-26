#!/usr/bin/python3

"""
Module to fetch content from a URL using urllib.request.

This module contains functionality to fetch the content of a
URL using the urllib.request module.
"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # Fetching the URL and reading the response
    with urllib.request.urlopen(url) as response:
        response_body = response.read()
        utf8_content = response_body.decode('utf-8')

    # Displaying the body of the response with tabulation
    print("- Body response:")
    print("\t- type:", type(response_body))
    print("\t- content:", response_body)
    print("\t- utf8 content:", utf8_content)
