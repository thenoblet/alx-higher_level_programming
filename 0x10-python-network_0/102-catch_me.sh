#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me_3 that causes the server to respond with a message containing You got me!
curl 0.0.0.0:5000/catch_me -sLX PUT -d "user_id=98" -H "Origin: School"
