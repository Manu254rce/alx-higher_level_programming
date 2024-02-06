#!/usr/bin/python3
"""
This is Python3 code
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr) for attr in attrs if attr in self.__dict__}
