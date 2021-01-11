#!/usr/bin/python3
"""
This module contains a function
which prints a square
with an int as size
"""


def print_square(size):
    if type(size) is not int:
        raise TypeError ("size must be an integer")
    if type(size) is bool:
        raise TypeError ("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError ("size must be an integer")
    if size < 0:
        raise ValueError ("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
    if size == 0:
        print()
