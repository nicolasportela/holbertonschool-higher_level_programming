#!/usr/bin/python3

"""Checks if the object is an instance of a class that inherited
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):

    """True if it is, False otherwise"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
