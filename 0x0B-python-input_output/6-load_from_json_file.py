#!/usr/bin/python3
"""this module contains a function that
creates an object from a JSON file"""


import json

def load_from_json_file(filename):
    """function to create the file"""

    with open(filename, encoding="UTF8") as file:
        return json.load(file)
