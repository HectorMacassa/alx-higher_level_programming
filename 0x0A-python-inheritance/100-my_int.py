#!/usr/bin/python3
"""
This module defines a class MyInt that inherits from pythons default int class.
"""


class MyInt(int):
    """
    This function has == and != operators inverted
    """
    def __eq__(self, value):
        """
        This function inverts the behaviour of the equality operator.

        Args:
            value (int): The integer value to be compared with

        Returns:
            bool: True if integer values are not equal, False otherwise
        """
        return self.real != value

    def __ne__(self, value):
        """
        This function inverts the behaviour of the equality operator.

        Args:
            value (int): The integer value to be compared with

        Returns:
            bool: True if integer values are equal, False otherwise
        """
        return self.real == value
