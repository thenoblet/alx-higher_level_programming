#!/usr/bin/python3

"""
Module to fetch and print the content of a URL.
This module contains functionality to fetch and print the content
of a URL provided as a command-line argument.
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
        with urllib.request.urlopen(sys.argv[1]) as request:
            response = request.read()
        print(response.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
