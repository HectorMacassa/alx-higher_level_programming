#!/usr/bin/python3
class Square:
    """Defines a square"""
   
   def __init___(self, size=0):
        """Initializes a new square.

        Args:
            size (int): Size of the square

        """
        self.__size = size

    @property
    def size(self):
        """Getter to obtain size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to obtain size of square

        Args:
            value (int): Value given

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
