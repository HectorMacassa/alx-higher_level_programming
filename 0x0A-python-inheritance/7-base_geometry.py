#!/usr/bin/python3
"""This module defines a class BaseGeometry"""


class BaseGeometry:
    """This class represents BaseGeometry"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates given value

        Args:
            name (str): The name of the parameter
            value (int): Value to be validated
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
