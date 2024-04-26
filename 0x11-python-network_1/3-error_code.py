#!/usr/bin/python3

"""
Module to fetch and print the content of a URL.

This module contains functionality to fetch and print the content
of a URL provided as a command-line argument.
"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
