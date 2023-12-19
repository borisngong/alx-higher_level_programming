#!/usr/bin/python3
"""Module for working a square"""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of one side of the square.
        __position (tuple): The position of the square.

    Raises:
        TypeError: If the provided size or position is invalid.
        ValueError: If the provided size or position is less than 0.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object.

        Args:
            size (int, optional): The size of one side of the square.
            Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If the provided size or position is invalid.
            ValueError: If the provided size or position is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of one side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of one side of the square.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the provided position is not a tuple of
            2 positive integers.
            ValueError: If the provided position is invalid.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' and position.

        If size is equal to 0, an empty line is printed.
        Position is used to determine the starting point of the square.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
