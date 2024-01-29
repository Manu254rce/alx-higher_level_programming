#!/usr/bin/python3
"""
This is a Python class
"""


class Rectangle:
    """
    This class contains function that defines
    attributes of a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        This is a initializer function for the rectangle's
        attributes

        Args:
            @width (int): the width of the rectangle
            @height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This function gets the private attribute width
        """
        return self.__width

    @property
    def height(self):
        """
        This is the getter function for the height attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        This function defines the width of the class with exception
        handling
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        This function sets the height attribute to value
        with exception handling
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
