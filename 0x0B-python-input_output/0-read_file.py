#!/usr/bin/python3
"""
This is a Python function
"""


def read_file(filename=""):
    """
    Function that returns contents read from a file
    with utf-8 encoding
    """
    with open(filename, encoding='utf-8') as file:
        print("{}".format(file.read(), end=''))
