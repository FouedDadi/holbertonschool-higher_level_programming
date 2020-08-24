#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""
import requests
from sys import argv


if __name__ == "__main__":
        requst = requests.get('https://api.github.com/user',
                              auth=(argv[1], argv[2]))
        print(requst.json().get('id'))
