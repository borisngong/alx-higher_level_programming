#!/usr/bin/python3
"""A module for working with squares"""


class Square:
    """A class representing a square"""
    def __init__(self, size=0):
        """Initializes a square oblect"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
