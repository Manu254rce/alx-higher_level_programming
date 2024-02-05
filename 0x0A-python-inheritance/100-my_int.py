#!/usr/bin/python3
"""
This is a Python class
"""


class MyInt(int):
    """
    This is a class that inherits from int and inverts
    logical operators
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
