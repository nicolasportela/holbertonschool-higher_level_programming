#!/usr/bin/python3

"""checks if an object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):

    """True if it is an instance, False otherwise"""
    return type(obj) == a_class
