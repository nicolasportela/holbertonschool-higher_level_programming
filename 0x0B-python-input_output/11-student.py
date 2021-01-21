#!/usr/bin/python3
"""this module writes a class named Student"""

import json


class Student:
    """class creation"""

    def __init__(self, first_name, last_name, age):
        """instantiation"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""

        if attrs is not None:
            new_dict = {}
            for obj in attrs:
                if type(obj) is not str:
                    return self.__dict__
                if obj in self.__dict__:
                    new_dict[obj] = self.__dict__[obj]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the instance"""

        for key, value in json.items():
            self.__dict__[key] = value
