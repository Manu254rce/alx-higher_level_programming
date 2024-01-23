#!/usr/bin/python3
"""
This is a Python class initialization with name `Square`
"""


class Square:
    """
    This class contains about five functions:
    - the custom constructor that defines a private
    instance
    - the getter and setter functions
    - the function that ccalculates the area of the
    square
    -the function that prints ASCII characters for
    the square
    """
    def __init__(self, size=0):
        """
        Function that defines the custom constructor
        """
        self._size = size

    @property
    def size(self):
        """
        Property getter function
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Property setter function with safe setting via
        exception handling
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        This function prints the area
        """
        return self._size ** 2

    def my_print(self):
        """
        This function prints the squares based on the
        size
        """
        if int(self._size) == 0:
            print()
        for i in range(self._size):
            for j in range(self._size):
                print("#", end="")
            print()
