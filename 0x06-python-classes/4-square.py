#!/usr/bin/python3
"""
This is a Python class initialization
"""


class Square:
    """
    This class contains four functions, a custom
    constructor, a property getter, a setter and
    a function that calculates the area of the size
    """
    def __init__(self, size=0):
        """
        This is a custom constructor
        """
        self._size = size

    @property
    def size(self):
        """
        This function retrieves a private class
        instance from the constructor
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        This function sets the retrieved private instance to
        a value and performs exception handling to ensure safe
        passing
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        This function will calculate the area of the function
        """
        return self._size ** 2
