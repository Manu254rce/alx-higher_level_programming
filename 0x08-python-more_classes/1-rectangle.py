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
        self._width = width
        self._height = height
