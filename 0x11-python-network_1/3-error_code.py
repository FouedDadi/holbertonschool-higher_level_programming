#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as reponse:
                print(reponse.read().decode('UTF-8'))
    except urllib.error.HTTPError as error:
        print('Error code: {:}'.format(error.code))
