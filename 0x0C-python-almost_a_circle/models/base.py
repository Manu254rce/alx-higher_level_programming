#!/usr/bin/python3
"""
This is Python3 code
"""


class Base:
    """
    This is a Python class which is the 'base' class in this for
    other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Function that initializes attributes
        """
        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
