#!/usr/bin/python3
"""this module contains a function to read a text file"""


def read_file(filename=""):
    """function to read a text file"""

    with open(filename, encoding="UTF8") as file:
        print(file.read())
