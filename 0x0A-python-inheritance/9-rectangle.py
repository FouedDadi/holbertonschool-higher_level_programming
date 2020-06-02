#!/usr/bin/python3
"""
importing 7-base_geometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle that inherets from BaseGeometry
    """

    def __init__(self, width, height):
        """
        initialisation
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        return area
        """
        return self.__height * self.__width

    def __str__(self):
        """
        string representation
        """
        return (f"[rectangle] {self.__width}/{self.__height}")
