#!/usr/bin/python3
"""This module contains the base class of all other classes in this project."""


import json


class Base:
    """parent class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list(list_dictionaries))

    # ARREGLAR ESTO, 16 #
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + '.json'
        myList = []
        with open(filename, "w", encoding="UTF8") as myFile:
            if list_objs is None:
                myFile.write(myList)
            else:
                for obj in list_objs:
                    myList.append(obj.to_dictionary())
                myFile.write(cls.to_json_string(myList))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    # ARREGLAR ESTO, 18 #
    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        sq_dummy = cls(4, 3, 2, 1)
        cls.update(sq_dummy, **dictionary)
        return sq_dummy

    # ARREGLAR ESTO, 19 #
    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        inst_list = []
        filename = cls.__name__ + '.json'
        if not filename:
            return inst_list
        else:
            with open(filename, "r", encoding="UTF8") as file:
                objs = cls.from_json_string(file.read())
                for obj in objs:
                    inst_list.append(cls.create(**obj))
                return inst_list
