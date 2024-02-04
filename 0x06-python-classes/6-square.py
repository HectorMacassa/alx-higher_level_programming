#!/usr/bin/python3
"""This modules defines a class Square"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square

        Args:
            size (int): Size of the square
            position (int, int): Position of the square

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i > 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(1, self.__position[1] + 1):
            print()
        for i in range(1, self.__size + 1):
            print(" " * self.__position[0] + "#" * self.__size)
