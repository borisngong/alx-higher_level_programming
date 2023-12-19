#!/usr/bin/python3
"""A module for working with squares."""


class Square:
    """A class representing a square.

    This class provides methods and attributes to work with square objects.
    """

    def __init__(self, size):
        """Initialize a square object.

        Args:
            size (int): The length of a side of the square.
        """
        self.__size = size
