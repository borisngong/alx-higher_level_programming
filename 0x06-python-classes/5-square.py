#!/ust/bin/python3
"""Module for working with a square"""


class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of one side of the square.

    Raises:
        TypeError: If the provided size is not an integer.
        ValueError: If the provided size is less than 0.
    """

    def __init__(self, size=0):
        """Initialize a square object.

        Args:
            size (int, optional): The size of one side of the square.
            Defaults to 0.

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        self.size = size

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

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.

        If size is equal to 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
