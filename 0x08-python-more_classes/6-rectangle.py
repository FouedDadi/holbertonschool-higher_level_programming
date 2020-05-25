#!/usr/bin/python3
"""
creating class rectangle
"""


class Rectangle:
    """
    attributes:
    height
    weight
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """
        return width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        returns area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        returns perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        return rectangle in "#"
        """
        stri = ''
        if (self.__height) == 0 or (self.__width) == 0:
            return stri
        for hor in range(self.__height):
            for ver in range(self.__width):
                stri = stri + "#"
            if hor < self.__height:
                stri = stri + "\n"
        return stri[:-1]

    def __repr__(self):
        """
        return string representation
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        print message when deleting
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
