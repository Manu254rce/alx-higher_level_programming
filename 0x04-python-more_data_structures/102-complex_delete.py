#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    else:
        for key in list(a_dictionary):
            if a_dictionary[key] == value:
                del a_dictionary[key]

        return a_dictionary
