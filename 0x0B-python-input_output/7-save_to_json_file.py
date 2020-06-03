#!/usr/bin/python3
"""
function that writes an obj to a text file using json rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writing to a text file
    """

    with open(filename, mode='w', encoding="UTF8") as myfile:
        return myfile.write(json.dumps(my_obj))
