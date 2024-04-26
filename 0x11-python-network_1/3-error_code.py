#!/usr/bin/python3

"""
Module to fetch and print the content of a URL.

This module contains functionality to fetch and print the content
of a URL provided as a command-line argument.
"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <URL>")
        sys.exit(1)

    url = sys.argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
