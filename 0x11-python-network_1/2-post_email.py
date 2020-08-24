#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as reponse:
        print(reponse.read().decode('UTF-8'))
