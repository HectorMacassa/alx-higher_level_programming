#!/usr/bin/python3
"""
This module defines a function that writes a string to a file.
The function creates a file if it doesn't exist.
The function overwrites content if it already exists
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a file

    Args:
        filename (str): The file to be written to
        text (str): The string to be written

    Returns:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
