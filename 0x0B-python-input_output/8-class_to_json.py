#!/usr/bin/python3
"""this module contains a function to return
the dictionary description with a simple data structure"""


def class_to_json(obj):
    """function"""

    return obj.__dict__
