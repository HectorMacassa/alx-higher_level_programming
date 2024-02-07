#!/usr/bin/python3
"""
This module defines a function that inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): The name of the file
        search_string (str): The string to search for in each line
        new_string (str): The string to insert after each line
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
