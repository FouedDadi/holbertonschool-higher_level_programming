#!/usr/bin/python3
"""
function that write a str to a file
"""


def write_file(filename="", text=""):
    """
    writing to a file
    """

    with open(filename, mode='w', encoding="UTF8") as myfile:
        return myfile.write(text)
