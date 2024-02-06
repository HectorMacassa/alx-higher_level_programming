#!/usr/bin/python3
"""
This module defines a function that returns the JSON representation 
of an object
"""
import json


def to_json_string(my_obj):
    """
    This function returns the JSON representation of an object

    Args:
        my_obj (str, int, list): Object to be converted
    """
    return json.dumps(my_obj)
