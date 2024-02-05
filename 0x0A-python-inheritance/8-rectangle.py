#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
