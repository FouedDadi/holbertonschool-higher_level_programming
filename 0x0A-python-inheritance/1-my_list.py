#!/usr/bin/python3
"""
creating class MyList
"""

class MyList(list):
    """
    public instnace method
    """

    def print_sorted(self):
        """
        print list
        """

        print(sorted(self))
