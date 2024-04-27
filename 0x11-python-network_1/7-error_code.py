#!/usr/bin/python3

"""
Module to fetch and print the content of a URL using requests.

This module contains functionality to fetch and print the content of a
URL provided as a command-line argument using the requests library.

Dependencies:
    - requests
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
