#!/usr/bin/python3
"""
This module defines a class Student
"""


class Student:
    """This class represents a student"""
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the instance"""
        if attrs is None:
            return self.__dict__

        result = {}
        for attribute in sorted(attrs):
            if hasattr(self, attribute):
                result[attribute] = getattr(self, attribute)
        return result

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for dict_key, key_value in json.items():
            setattr(self, dict_key, key_value)
