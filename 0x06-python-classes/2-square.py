#!/usr/bin/python3


""" this class defines a square that has a Private instance attribute size"""


class Square:

    """ Instantiation with optional size """

    def __init__(self, size=0):

        """size is private attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
