#!/usr/bin/python3
"""This module checks for inherited class instance"""

def inherits_from(obj, a_class):
    """Checks if object is an instance of a class that inherited from the specified class"""

    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    return False
