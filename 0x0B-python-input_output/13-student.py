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

    def to_json(self, attrs=None):
        """
        returning dict desc
        """
        mydict = {}
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            for key, value in self.__dict__.items():
                if key in attrs:
                    mydict[key] = value
            return mydict
        return self.__dict__

    def reload_from_json(self, json):
        """
        replace all attributes
        """

        for key, value in json.items():
            self.__dict__[key] = value
