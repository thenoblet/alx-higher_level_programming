#!/usr/bin/python3

"""
Module to fetch and print the content of a URL using the
requests library.

This module contains functionality to fetch and print the content
of a URL using the requests library.

Dependencies:
    - requests
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    response_body = response.text
    response_type = type(response_body)

    print("Body response:")
    print("\t- type:", response_type)
    print("\t- content:", response_body)
