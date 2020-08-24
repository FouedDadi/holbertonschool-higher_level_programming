#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    requst = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {:}".format(type(requst.text)))
    print("\t- content: {:}".format(requst.text))
