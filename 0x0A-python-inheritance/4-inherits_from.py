#!/usr/bin/python3
"""
function to check if obj is instance of a class that inherited from a_class
"""


def inherits_from(obj, a_class):
    """
    return True or False
    """

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
