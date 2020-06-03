#!/usr/bin/python3
"""
function that returns an object from json rep
"""
import json


def from_json_string(my_str):
    """
    returning obj
    """

    return json.loads(my_str)
