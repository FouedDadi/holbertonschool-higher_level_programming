#!/usr/bin/python3
"""
add attribute
"""


def add_attribute(o, name, value):
    """
    add attribute
    """

    if hasattr(o, "__dict__"):
        setattr(o, name, value)
    else:
        raise TypeError("can't add new attribute")
