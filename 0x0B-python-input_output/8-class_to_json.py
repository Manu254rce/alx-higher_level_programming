#!/usr/bin/python3
"""
This is a Python code
"""


def class_to_json(obj):
    """
    Function that returns dictionary description of any
    Python object
    """
    return obj.__dict__
