#!/usr/bin/python3
"""
This module
writes a class
that defines a rectangle
"""


class Rectangle:
    """based on 3-rectangle.py"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """return the string"""
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for i in range(self.__height):
            for j in range(self.__width):
                rec = rec + "#"
            if i < (self.__height - 1):
                rec = rec + "\n"
        return rec

    def __repr__(self):
        """return the string"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
