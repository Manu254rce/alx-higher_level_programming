#!/usr/bin/python3
"""
This is a Python class
"""


class Rectangle:
    """
    This class contains functions that define the area
    and perimeter of a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter function for the width attribute
        """
        return self.__width

    @property
    def height(self):
        """
        Getter function for the height attribute
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Setter function for the width attribute, based on
        exception handling
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter function for the height attribute, with exception
        handling
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        """
        if self.__width and self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
