#!/usr/bin/python3
"""This module contains the class Square derivated from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""

        return self.width

    @size.setter
    def size(self, size):
        """size value"""

        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """overloading string representation"""

        s = "[Square] ({:d}) {:d}/{:d} - {:d}".format(
                                                    self.id,
                                                    self.x,
                                                    self.y,
                                                    self.size
                                                    )
        return s

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""

        list_attr = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        square_dict = {
                    "id": self.id,
                    "size": self.size,
                    "x": self.x,
                    "y": self.y
                    }
        return square_dict
