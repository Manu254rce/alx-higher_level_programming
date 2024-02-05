#!/usr/bin/python3


def add_attribute(obj, attr, value):
    """
    This function sets a new custom attribute for an object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
