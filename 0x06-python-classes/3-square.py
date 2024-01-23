#!/usr/bin/python3
"""
This is a Python class instance
"""


class Square:
    """
    This is a class that contains a function that
    defines and sets a property for an instance
    """
    def __init__(self, size=0):
        """
        This is the init function that instantiates the
        size variable in the class
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This is a method that retrieves the private
        instance and calclates its area
        """
        return self.__size ** 2
