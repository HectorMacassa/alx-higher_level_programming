#!/usr/bin/python3
"""
This module defines a class Base
"""
import json


class Base:
    """
    Base class for other objects

    Attributes:
        __nb_objects (int): Number of instantiated objects.
        id (int): Unique identifier of objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int): Unique identifier of objects. Default = None.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON striing representation of a list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the JSON string representation of a list of objects to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base
        """

        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        json_string = cls.to_json_string(list_objs)

        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        json_list = []
        if json_string is None:
            return json_list
        else:
            json_list = json.loads(json_string)
            return json_list

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances of the class,
            or an empty list if the file doesn't exist.
        """

        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                instances = cls.from_json_string(json_string)
                return instances
        except FileNotFoundError:
            return []
