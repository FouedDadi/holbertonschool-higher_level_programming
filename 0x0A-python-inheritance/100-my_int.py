#!/usr/bin/python3
"""
function that inverts operators
"""


class MyInt(int):
    """
    class MyInt that inherets from int
    """

    def __eq__(self, integer):
        """
        invert equality
        """

        return not int.__eq__(self, integer)

    def __ne__(self, integer):
        """
        invert not eqaulity
        """

        return not int.__ne__(self, integer)
