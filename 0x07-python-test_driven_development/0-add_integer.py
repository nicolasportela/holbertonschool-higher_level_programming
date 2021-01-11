#!/usr/bin/python3
"""
This module contains the add function.
It returns an integer from the sum of a and b
or raises TypeError if any of them are not int or float.
"""


def add_integer(a, b=98):
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(a) is bool:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(b) is bool:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
