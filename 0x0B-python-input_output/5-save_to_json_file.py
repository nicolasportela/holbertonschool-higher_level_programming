#!/usr/bin/python3
"""this module contains a function that writes an object
to a text file via JSON representation"""


import json

def save_to_json_file(my_obj, filename):
    """function to write"""

    with open(filename, "w", encoding="UTF8") as file:
        f = json.dumps(my_obj)
        file.write(f)
