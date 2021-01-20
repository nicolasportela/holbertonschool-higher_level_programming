#!/usr/bin/python3

"""This module writes a class"""


class BaseGeometry():

    """Contains public instances methods"""

    def area(self):

        """Raise an exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """It validates value"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
