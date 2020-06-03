#!/usr/bin/python3
"""
creating class Student
"""


class Student:
    """
    class Student created
    """

    def __init__(self, first_name, last_name, age):
        """
        initialisation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returning dict desc
        """

        return self.__dict__
