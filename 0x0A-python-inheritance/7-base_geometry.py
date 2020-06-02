#!/usr/bin/python3
"""
creating class BaseGeometry
"""


class BaseGeometry:
    """
    Public instance method
    """

    def area(self):
        """
        raise an exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        check if value is int and bigger than 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
