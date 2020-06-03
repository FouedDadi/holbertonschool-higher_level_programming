#!/usr/bin/python3
"""
function that returns number of lines in file
"""


def number_of_lines(filename=""):
    """
    return number of lines
    """
    number = 0
    with open(filename, mode='r') as myfile:
        for line in myfile:
            number = number + 1
        return number
