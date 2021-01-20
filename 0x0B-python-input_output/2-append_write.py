#!/usr/bin/python3
"""this module contains a function
to append a string at the end of a text file"""


def append_write(filename="", text=""):
    """function to append at the end"""

    with open(filename, "a", encoding="UTF8") as file:
        return file.write(text)
