#!/usr/bin/python3
"""this module contains a function that returns
the JSON representation of an object"""


import json

def to_json_string(my_obj):
    """function to return a JSON representation"""
    return json.dumps(my_obj)
