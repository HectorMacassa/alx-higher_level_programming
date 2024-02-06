#!/usr/bin/python3
"""
This module is a script that adds all arguments to a Python list,
and then save them to a file.

If the file doesn't exist it must be created
"""
import json
import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args):
    """
    This function checks if file exists, adds arguments to the list
    and saves the list to JSON file
    """
    file_name = "add_item.json"
    data = []
    if path.exists(file_name):
        data = load_from_json_file(file_name)
    data.extend(args)
    save_to_json_file(data, file_name)

if __name__ == "__main__":
    add_item(sys.argv[1:])
