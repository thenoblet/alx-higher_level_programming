#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" "$1" --data @"$2"
