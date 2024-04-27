#!/usr/bin/python3

"""
Module to retrieve the GitHub user ID using the provided username and password.

This module retrieves the GitHub user ID by sending a GET request to the GitHub API
with the provided username and password for authentication.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)
