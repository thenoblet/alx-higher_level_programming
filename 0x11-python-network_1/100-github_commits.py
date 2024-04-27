#!/usr/bin/python3

"""
Module to fetch and print recent commits from a GitHub repository.

This module retrieves the recent commits from a GitHub repository
specified by the repository name and owner name provided
as command-line arguments.

Usage:
     <repo_name> <owner_name>
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construct the URL for the GitHub API to fetch commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)
