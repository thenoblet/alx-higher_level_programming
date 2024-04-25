#!/bin/bash
# This script prints the allowed http methods a server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
