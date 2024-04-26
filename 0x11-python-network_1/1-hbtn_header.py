#!/usr/bin/python3

"""
Module to retrieve the X-Request-Id header value from a given URL.

This module contains functionality to fetch the X-Request-Id
header value from a URL provided as a command-line argument.

Usage:
    ./1-hbtn_header.py <url>
"""

import urllib.request
import sys

if __name__ == "__main__":
    # Get the URL from command-line arguments
    url = sys.argv[1]

    # Fetching the URL and reading the response headers
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
