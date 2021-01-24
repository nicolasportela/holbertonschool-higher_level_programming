#!/usr/bin/python3
"""This module contains the base class of all other classes in this project."""

class Base:
    """parent class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects