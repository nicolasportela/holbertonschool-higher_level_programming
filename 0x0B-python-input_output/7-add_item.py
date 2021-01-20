#!/usr/bin/python3
"""script to add all arguments to a Python list
and save them to a file"""


import save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import load_from_json_file = __import__('6-load_from_json_file').\
                             load_from_json_file
import json
from sys import argv


try:
    json_list = load_from_json_file("add_item.json")
except:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, "add_item.json")
