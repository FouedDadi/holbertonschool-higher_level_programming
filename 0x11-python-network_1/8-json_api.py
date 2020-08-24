#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
        if len(argv) <= 1:
            q = ""
        else:
            q = argv[1]
        requst = requests.post('http://0.0.0.0:5000/search_user',
                               data={'q': q}).json()
        if requst == {}:
            print('No result')
        elif requst != {}:
            print('[{:}] {:}'.format(requst.get('id'), requst.get('name')))
        else:
            print('Not a valid JSON')
