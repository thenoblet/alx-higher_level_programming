#!/usr/bin/python3

"""
Module to retrieve the value of the X-Request-Id header
from a URL using requests.

This module contains functionality to retrieve the value
of the X-Request-Id header from a URL provided as a command-line
argument using the requests library.

Dependencies:
    - requests
"""

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
