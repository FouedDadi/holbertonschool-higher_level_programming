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
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 and value[1] < 0:
            self.__position = value
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
            print(' ' * self.__position[0], end='')
            print("#" * self.__size)
        for x in range(self.__position[1]):
            print()
        if self.__size == 0:
            print("")
