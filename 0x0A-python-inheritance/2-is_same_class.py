#!/usr/bin/python3
"""This modules defines a function that checks instances"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj (Object): The objected to be checked
        a_class (class): The class to be checked against

    Returns:
        bool: True if succesful, False otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
