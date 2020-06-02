#!/usr/bin/python3
"""
add attribute
"""


def add_attribute(o, name, value):
    """
    add attribute
    """

    if not hasattr(o, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(o, name, value)
