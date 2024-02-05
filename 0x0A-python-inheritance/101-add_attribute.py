#!/usr/bin/python3
"""
This is a Python function
"""


def add_attribute(obj, attr, value):
    """
    This function sets a new custom attribute for an object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr, value)
