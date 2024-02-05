#!/usr/bin/python3
"""This module defines a class Square the inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class represents a Square"""

    def __init__(self, size):
        """
        Initializes a new square

        Args:
            size (int): The size of the square

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
