#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a Rectangle class inheriting BaseGeometry"""

    def __init__(self, width, height):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.__width = width
        self.__height = height

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
