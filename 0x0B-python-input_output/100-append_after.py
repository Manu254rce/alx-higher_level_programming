#!/usr/bin/python3
"""
This is some Python3 code
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that appends or inserts a line into the end of a
    text file after specific characte
    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] = line + new_string
        file.seek(0)
        file.writelines(lines)
