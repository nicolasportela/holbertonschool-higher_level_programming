#!/usr/bin/python3
"""this module writes a class named Student"""


class Student:
    """class creation"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""

        self.first_name = first
        self.last_name = last
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation"""

        return (self.__dict__)
