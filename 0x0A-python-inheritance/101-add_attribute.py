#!/usr/bin/python3
"""This module defines a class add_attribute"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds anew attribute to an object if possible, otherwise raises a TypeError

    Args:
        obj: The object to which the attribute will be added
        attr_name: The name of the attribute to be added
        attr_value: The value of the attribute to be added

    Raises:
        TypeError: If the object cannot have a new attribute added
    """
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr_name] = attr_value
    elif hasattr(type(obj), '__dict__'):
        setattr(type(obj), attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
