#!/usr/bin/python3

"""
Module to send a POST request with email as a parameter to a
URL using requests.

This module contains functionality to send a POST request with an
email parameter to a URL provided as a command-line argument along
with the email address using the requests library.

Dependencies:
    - requests
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})
    print(response.text)
