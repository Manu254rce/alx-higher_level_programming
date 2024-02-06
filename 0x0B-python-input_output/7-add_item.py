#!/usr/bin/python3
"""
This is a Python3 code
"""


import json
from sys import argv
from importlib import import_module


file = 'add_item.json'

save_json = import_module('5-save_to_json_file').save_to_json_file
load_json = import_module('6-load_from_json_file').load_from_json_file

try:
    obj = load_json(file)
except (FileNotFoundError, json.JSONDecodeError):
    obj = []

obj.extend(argv[1:])
save_json(obj, file)
