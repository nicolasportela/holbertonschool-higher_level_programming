#!/usr/bin/python3
"""
This module contains a function
which prints
a first name and a last name.
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(first_name) is bool:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if type(last_name) is bool:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
