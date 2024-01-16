#!/ust/bin/python3
"""Module responsible for working with Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square inheriting from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """String representation"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width)
        )

    def update(self, *args, **kwargs):
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """A dictionary representation of a Square"""
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict
