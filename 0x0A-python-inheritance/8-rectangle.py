#!/usr/bin/python3

"""This module writes a derivated class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """derivated from BaseGeometry"""
    def __init__(self, width, height):

        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
