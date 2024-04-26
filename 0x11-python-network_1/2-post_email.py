#!/usr/bin/python3

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Sending a POST request with the email as a parameter
    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
