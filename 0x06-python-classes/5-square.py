#!/usr/bin/python3


""" this class defines a square that has a Private instance attribute size"""


class Square:

    """Instantiation with optional size"""

    def __init__(self, size=0):

        """size is private attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):

        """getting the value"""
        return self.__size

    @size.setter
    def size(self, value):

        """setting the value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ print square with #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
