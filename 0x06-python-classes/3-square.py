#!/usr/bin/python3
"""Module for working with a square"""


class Square:
    """A class representing a square"""
    def __init__(self, size=0):
        """Initialize a square object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
