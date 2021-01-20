#!/usr/bin/python3

"""This module writes a derivated class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """derivated from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """calculates the area of the square"""
        return (self.__size * self.__size)
