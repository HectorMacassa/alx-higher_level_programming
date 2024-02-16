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
        Returns the JSON string representation of a list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves the JSON string representation of a list of objects to a file.
        Args:
            list_objs (list): A list of instances inheriting from Base
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns a new list of the JSON string rep"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances of the class,
            or an empty list if the file doesn't exist.
        """
        filename = cls.__name__ + "j.son"
        try:
            with open(filename, "r") as file:
                json_string = cls.from_json_string(file.read())
                return [cls.create(**d) for i in json_string]
        except FileNotFoundError:
            return []
