#!/usr/bin/python3
"""
creating a class Rectangle that inherets from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle created
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialisation
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        return width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setts wdith attribute
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        return height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setts height attribute
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """
        return x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setts x attribute
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):

        """
        return y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setts y attribute
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        returns are
        """
        return self.__height * self.__width

    def display(self):
        """
        print rectangle with # character
        """
        if self.width == 0 or self.height == 0:
            return ''
        for w in range(self.__height):
            for w in range(self.__x):
                print(' ', end='')
            print('#' * self.__width, end='')
            print('' * self.__y)

    def __str__(self):
        """
        return str representation of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        updating rectangle
        """

        attributes = ["id", "width", "height", "x", "y"]
        for w in range(len(args)):
            setattr(self, attributes[w], args[w])
        if len(args) > 0 and args is not None:
            pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        disctionary representation of rectangle
        """

        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
