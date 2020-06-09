#!/usr/bin/python3
"""
creating a class Square that inherets from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square created
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialisation Square
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        return size attribute
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        setts wdith attribute
        """

        self.width = value
        self.height = value

    def __str__(self):
        """
        return str representation of the rectangle
        """
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.size)

    def update(self, *args, **kwargs):
        """
        updating square
        """

        attributes = ["id", "size", "x", "y"]
        for x in range(len(args)):
            setattr(self, attributes[x], args[x])
        if len(args) > 0 and args is not None:
            pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        dictionary representation of a square
        """

        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
