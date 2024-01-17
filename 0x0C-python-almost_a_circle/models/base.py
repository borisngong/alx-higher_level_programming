#!/usr/bin/python3
"""Module for working with the base class"""
import json


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

    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
