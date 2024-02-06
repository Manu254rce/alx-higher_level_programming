#!/usr/bin/python3
"""
This is Python3 code
"""


class Student:
    """
    This cclass defines functions that define and
    return dictinary list for Student attributes
    """
    def __init__(self, first_name, last_name, age):
        """
        Function that is a class constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function that returns dictionary structure for
        student attributes
        """
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs
                if attr in self.__dict__}
