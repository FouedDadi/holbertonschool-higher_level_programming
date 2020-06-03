#!/usr/bin/python3
"""
function that append a strig to a file
"""


def append_write(filename="", text=""):
    """
    appending to a file
    """

    with open(filename, mode='a', encoding="UTF8") as myfile:
        return myfile.write(text)
