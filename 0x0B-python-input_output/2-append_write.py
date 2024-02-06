#!/usr/bin/python3
"""
This module defines a function that appends a string at the end of a text file.
If the file doesn’t exist, it should be created.
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of text file

    Args:
        filename (str): filename to be appended or created
        text (str): String to be appended to text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
