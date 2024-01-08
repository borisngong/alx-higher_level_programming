#!/usr/bin/python3
"""Defines a function for looking up an object's attributes"""


class MyList(list):
    """Return a list of available attributes of an object."""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
