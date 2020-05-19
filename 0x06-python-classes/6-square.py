#!/usr/bin/python3
"""
define a class Square
"""


class Square:
    """
    class Square with private instance attribute size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        size = size
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        retrieve position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        set the position
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) < 0 or type(value[1]) < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        return the square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        print the square with the character #
        """
        for x in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
