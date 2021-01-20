#!/usr/bin/python3
"""this module contains a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """function to write to a text file"""

    with open(filename, "w", encoding="UTF8") as file:
        return file.write(text)
