#!/usr/bin/python3
"""Module for working Squares"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square inheriting from Rectangle claa instance"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor: Initializes size, x, y, id attributes"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Setter for attribute size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides __str__ method to return string representation"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        ))
