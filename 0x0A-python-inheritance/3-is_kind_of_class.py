#!/usr/bin/python3
"""This module checks the instance of an object"""

def is_kind_of_class(obj, a_class):
    """
    This function checks if the object is an instance of, 
    or if the object is an instance of a class that inherited from
    the specified class
    """

    if isinstance(obj, a_class):
        return True
    return False
