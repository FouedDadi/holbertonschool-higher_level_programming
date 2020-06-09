#!/usr/bin/python3
"""
creating a class base
"""
import json
from os import path


class Base:
    """
    class base created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialisation
        """
        if id is None:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return json string representation of list of dictionary
        """

        if list_dictionaries is not None or len(list_dictionaries) > 0:
            return json.dumps(list_dictionaries)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write the JSON string representation of list_objs to a file
        """

        mylist = []
        with open(cls.__name__ + ".json", mode="w") as myfile:
            for o in list_objs:
                mylist.append(o.to_dictionary())
            myfile.write(Base.to_json_string(mylist))
            if list_objs is None:
                myfile.write("[]")

    @staticmethod
    def from_json_string(json_string):
        """
        return the list of the JSON string representation
        """

        if json_string is not None or len(json_string) > 0:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """

        if cls.__name__ == "Square":
            nw = cls(5)
            nw.update(**dictionary)
        if cls.__name__ == "Rectangle":
            nw = cls(5, 5)
            nw.update(**dictionary)
        return nw

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """

        my_list = []
        filename = cls.__name__ + ".json"
        if path.exists(filename) is False:
            return []
        with open(filename, mode="r") as my_file:
            objects = cls.from_json_string(my_file.read())
            for dicts in objects:
                creation = cls.create(**dicts)
                my_list.append(creation)
            return my_list
