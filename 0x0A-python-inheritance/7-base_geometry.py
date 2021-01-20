#!/usr/bin/python3

"""This module writes a class"""


class BaseGeometry():

    """Contains public instances methods"""

    def area(self):

        """Raise an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """It validates value"""
        if type(name) is not str:
            raise TypeError("name must be a string")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
