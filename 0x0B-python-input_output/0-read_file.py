#!/usr/bin/python3
"""
function that reads file
"""


def read_file(filename=""):
    """
    opening and reading
    """

    with open(filename, encoding="UTF8") as myfile:
        print(myfile.read(), end="")
