#!/usr/bin/python3
"""
This is a Python class
"""


class Rectangle:
    """
    This class contain fuctions that define a
    Rectangle and finds its area, perimeter and
    directs some output to __str__, as well as an aditional __repr__
    fallback function
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the class attributes for the
        rectangle
        """
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
        Setter functon for the width attribute
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter functon for the height attribute
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        This function calculates the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This function returns the perimeter of the
        rectangle
        """
        if self.__width and self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Function that prints formatted strings according
        to rectangle attributes
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#"*self.__width]*self.__height)

    def __repr__(self):
        """
        Fallback function for the string formatting
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
