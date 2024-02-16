#!/usr/bin/python3

"""
Unit tests for classes Base, Rectangle, and Square in a modeling system.
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test suite for the Base class
    """

    def test_constructor(self):
        """
        Test base constructor method
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)

        b3 = Base()
        b4 = Base()
        self.assertEqual(b3.id, 2)
        self.assertEqual(b4.id, 3)


class TestToJsonString(unittest.TestCase):
    """
    Unit tests for the to_json_string method
    """

    def test_to_json_string(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

        list_dicts = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        json_str = Base.to_json_string(list_dicts)
        expected_str = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(json_str, expected_str)


class TestFromJsonString(unittest.TestCase):
    """
    Unit tests for the from_json_string method
    """

    def test_from_json_string_empty_string(self):
        json_string = "[]"
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid_json(self):
        json_string = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        result = Base.from_json_string(json_string)
        expected = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        self.assertEqual(result, expected)


class TestCreate(unittest.TestCase):
    """
    Unit tests for the create method
    """

    def test_create_original_square_instance(self):
        square_original = Square(5, 7, 2, 9)
        square_original_dict = square_original.to_dictionary()
        square_created = Square.create(**square_original_dict)
        self.assertEqual("[Square] (9) 7/2 - 5", str(square_original))


class TestBaseLoadFromFile(unittest.TestCase):
    """
    Unit tests for the load_from_file method
    """

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

    # Test methods for load_from_file...


if __name__ == '__main__':
    unittest.main()
