#!/usr/bin/python3

"""This module writes a derivated class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Square(Rectangle):
    """derivated from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """calculates the area of the square"""
        return (self.__size * self.__size)
