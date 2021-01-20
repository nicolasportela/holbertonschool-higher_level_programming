#!/usr/bin/python3
"""this module contains a function that returns
an object represented by JSON"""


import json

def from_json_string(my_str):
    """function that returns a JSON"""
    return json.loads(my_str)
