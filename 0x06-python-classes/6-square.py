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
        if type(value) is tuple and len(value) == 2:
            if type(value) is int:
                if value[0] > 0 and value[1] > 0:
                    self.__position = value
        raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """
        return the square area
        """
        return self.__size ** 2

def my_print(self):
        """ prints a square in # """
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print('#', end='')
            print("")
        if self.size == 0:
            print()

