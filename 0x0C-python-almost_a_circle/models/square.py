#!/usr/bin/python3
"""Represents a square with specific properties."""
import json

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a square with attributes for size, position, and optional ID.
    Inherits from the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The length of one side of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (str, optional): An optional identifier for the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
       """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overwrites the string method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.size = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y,
                }
