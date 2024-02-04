#!/usr/bin/python3
"""This modules defines a class square"""


class Square:
    """This class represents a square"""

    def __init__(self, size=0):
        """
        Initializes a new square

        Args:
            size (int): Size of the square

        """
        self.__size = size

    @property
    def size(self):
        """Getter to retrieve size"""
        self.__size = size

    @size.setter
    def size(self, value):
        """Setter to set value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        for i in range(1, self.__size + 1):
            print("#" * self.__size)
