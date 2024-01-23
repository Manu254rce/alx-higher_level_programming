#!/usr/bin/python3
"""
This is a Python class instance
"""


class Square:
    """
    This class contains five functions
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        This is a custom constructor
        Args:
            size(int): size of square
            position(tuple): coordinates of square
        """
        self._size = size
        self._position = position

    @property
    def size(self):
        """
        This is the size getter
        """
        return self._size

    @property
    def position(self):
        """
        This is a position getter
        """
        return self._position

    @size.setter
    def size(self, value):
        """
        This function sets size with some exception handling
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif int(value) < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @position.setter
    def position(self, value):
        """
        This is a position setter with some exception handling
        """
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be 2 positive integers")
        self._position = (value[0], value[1])

    def area(self):
        """
        This function prints area
        """
        return pow(self._size, 2)

    def my_print(self):
        """
        This function prints the square along with position
        coordinates
        """
        if self._size == 0:
            print()
        print('\n' * self._position[1], end='')
        for _ in range(self._size):
            print(' ' * self._position[0] + '#' * self._size)
