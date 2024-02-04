#!/usr/bin/python3
"""
This modules defines a class Square

"""


class Square:
    """
    This class represents a square

    Attributes:
        __size (int): The size of the square

    """
    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            __size (int) = Size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area size"""
        return (self.__size * self.__size)
