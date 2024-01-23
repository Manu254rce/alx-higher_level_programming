#!/usr/bin/python3
"""
This is an entry point for a Python class
"""


class Square:
    """
    This is a function that instantiats a private
    class instance and also implements exception handling
    """
    def __init__(self, size=0):
        self.__size = size
        if int(size) < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
