#!/usr/bin/python3
"""
This is code written in Python 3.4
"""


import json


def from_json_string(my_str):
    """
    This functin decodes JSON into string
    """
    return json.loads(my_str)
