#!/usr/bin/python3
"""This module defines a function that reads a text file"""


def read_file(filename=""):
    """
    This function reads a file and prints it to stdout

    Args:
        filename (str): File to be read
    """
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read(), end="")
