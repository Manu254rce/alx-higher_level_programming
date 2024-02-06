#!/usr/bin/python3
"""
This is a Python code
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text
    file, returning the count of chracters
    """
    count = 0
    with open(filename, 'a', encoding='utf-8') as file:
        for char in text:
            file.write(char)
            count += 1

    return count
