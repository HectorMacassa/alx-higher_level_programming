#!/usr/bin/python3
"""This module defines a Rectangle class that inherits froom Base"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with specific properties.

    Inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (str, optional): An optional identifier for the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0,
            or if x or y is negative.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for _ in range(self.__y):
            print()
        for i in range(self.__height):
            row = ""
            row += " " * self.__x
            row += "#" * self.__width
            print(row)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id(),
                                                       self.x(), self.y(),
                                                       self.width(),
                                                       self.height())

    def update(self, *args, **kwargs):

        for key, value in kwargs.items():
            if key == "id":
                self.__id = value
            elif key == "width":
                self.__width = value
            elif key == "height":
                self.__height = value
            elif key == "x":
                self.__x = value
            elif key == "y":
                self.__y = value

    def to_dictionary(self):

        return {
                "id": self.__id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y,
                }
