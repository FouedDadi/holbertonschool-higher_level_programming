#!/usr/bin/python3
"""
creating class lockedclass
"""


class LockedClass:
    """
    prevent user from creating instance class only if it's called first_name
    """
    __slots__ = ["first_name"]
