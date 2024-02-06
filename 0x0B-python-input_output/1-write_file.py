#!/usr/bin/python3
"""
This is code written in Python 3.4
"""


def write_file(filename="", text=""):
    """
    Function that creates a new file and writes new content,
    while counting the size of the string
    """
    count = 0
    with open(filename, 'w', encoding='utf-8') as file:
        for char in text:
            file.write(char)
            count += 1

    return count
