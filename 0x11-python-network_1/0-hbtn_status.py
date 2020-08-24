#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as reponse:
        bd = reponse.read()
        print("Body response:")
        print("\t- type: {:}".format(type(bd)))
        print("\t- content: {:}".format(bd))
        print("\t- utf8 content: {:}".format(bd.decode('utf-8')))
