#!/usr/bin/python3

"""
Script to fetch user ID from GitHub using Basic Authentication
with a personal access token
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
        # user_id = user_data.get('id')
        # print(user_id)
    else:
        print(None)
