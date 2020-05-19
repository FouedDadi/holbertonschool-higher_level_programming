#!/usr/bin/python3
import math


class MagicClass:
    """
    class magiclass
    """
    def __init__(self, radius):
        """
        initialization
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
