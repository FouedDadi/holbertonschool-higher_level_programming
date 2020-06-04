#!/usr/bin/python3
"""
script that adds all arguments to a Python list
"""
from sys import argv
import json


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

try:
    newlist = load_from_json_file('add_item.json')
except:
    newlist = list()
for a in range(len(argv)):
    newlist.append(argv[a])
save_to_json_file(newlist, 'add_item.json')
