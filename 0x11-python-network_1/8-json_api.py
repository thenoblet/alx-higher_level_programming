#!/usr/bin/python3

"""
Module to search for a user using a query parameter and print the result.

This module contains functionality to search for a user using a query
parameter and print the result obtained from the server.

Dependencies:
    - requests
"""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"

    response = requests.post(url, data={'q': q})
    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError:
        print("Not a valid JSON")
