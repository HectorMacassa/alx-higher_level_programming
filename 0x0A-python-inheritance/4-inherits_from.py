#!/usr/bin/python3
"""This module checks for inherited class instance"""


def inherits_from(obj, a_class):
    """
    Checks if object is an instance of a class that inherited from the specified class

    Args:
        obj: Object to be checked
        a_class: The class to be checked against

    Returns:
        bool: True if successsful, False if otherwise
    """

    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
