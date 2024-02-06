#!/usr/bin/python3
"""
This is Python3 code
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that saves an object into a JSON
    representation in text
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
