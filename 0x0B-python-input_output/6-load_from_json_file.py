#!/usr/bin/python3
"""
This is Python 3 code
"""


import json


def load_from_json_file(filename):
    """
    Function that creates an object from a JSON file
    """
    with open(filename) as file:
        stream = json.load(file)
    return stream
