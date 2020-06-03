#!/usr/bin/python3
"""
function that creates an obj from json file
"""
import json


def load_from_json_file(filename):
    """
    returning load
    """

    with open(filename) as myfile:
        return json.load(myfile)
