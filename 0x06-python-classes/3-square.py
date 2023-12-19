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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
