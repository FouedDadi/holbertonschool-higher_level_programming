#!/usr/bin/python3
"""
define a class Square
"""


class Square:
    """
    class Square with private instance attribute size
    """
    def __init__(self, size=0):
        """
        size = size
        """
        self.__size = size

    @property
    def size(self):
        """
        retrieve size
        """

        return self.__size

    @size.setter
    def size(self, size):
        """
        raise errors if size is not int or negative
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size >= 0:
            self.__size = size

        else:

            raise ValueError('size must be >= 0')

    def area(self):
        """
        return the square area
        """
        return self.__size ** 2

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __eq__(self, other):
        return self.__size == other.__size

    def __it__(self, other):
        return self.__size <= other.__size

    def __inf__(self, other):
        return self.__size < other.__size
