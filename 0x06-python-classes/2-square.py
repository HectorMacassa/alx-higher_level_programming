#!/usr/bin/python3
"""This module defines a square class"""

class Square:
    """This class represents a square"""

    def __init__(self, size=0):
        """Initializes a square with a default or set size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size
