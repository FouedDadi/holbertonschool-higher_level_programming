#!/usr/bin/python3
"""
function that adds two integers
"""


def add_integer(a, b=98):
    """
    handling errors before returning a + b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
