#!/usr/bin/python3
"""Module for working with the base class"""


class Base:
    """Base Class with private class attribute __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Class constructor: Initializes id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
