#!/usr/bin/python3
#Bash script that takes in a URL, sends a request to that URL,
#and displays the size of the body of the response
curl -sI "$URL" | grep -i Content-Length | cut -d " " -f2