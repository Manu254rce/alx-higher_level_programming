#!/usr/bin/python3
"""
This is Python3 code
"""


from models.base import Base


class Rectangle(Base):
    """
    Class that defines a rectangle based from the
    Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Function that initializes class attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter function for the width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function for the width attribute
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter function for the height attribute
        """
        return self.__height

    @property
    def x(self):
        """
        Getter function for the x attribute
        """
        return self.__x

    @property
    def y(self):
        """
        Getter function for the y attribute
        """
        return self.__y

    @height.setter
    def height(self, value):
        """
        Setter function for the height attribute
        """
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Setter function for the x attribute
        """
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter function for the y attribute
        """
        self.__y = value
