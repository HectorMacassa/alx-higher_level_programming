#!/usr/bin/python3

import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    def test_init(self):
        # Test valid initialization
        square = Square(5)
        self.assertEqual(square.id, Base.get_id())
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        # Test initialization with specific x and y
        square_xy = Square(7, x=2, y=3)
        self.assertEqual(square_xy.x, 2)
        self.assertEqual(square_xy.y, 3)

        # Test initialization with id
        square_id = Square(10, id=123)
        self.assertEqual(square_id.id, 123)

    def test_invalid_init(self):
        # Test invalid size (not int)
        with self.assertRaises(TypeError):
            Square("invalid")

        # Test invalid size (less than 0)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_size_setter(self):
        square = Square(5)

        # Test valid setter
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

        # Test invalid setter (not int)
        with self.assertRaises(TypeError):
            square.size = "invalid"

        # Test invalid setter (less than 0)
        with self.assertRaises(ValueError):
            square.size = -1

    def test_area(self):
        square = Square(10)
        self.assertEqual(square.area(), 100)

    def test_display(self):
        # Capturing output to compare
        with self.assertRaises(NotImplementedError):
            square = Square(10)
            square.display()

    def test_update(self):
        square = Square(10)

        # Test update with size
        square.update(size=15)
        self.assertEqual(square.size, 15)

        # Test update with other attributes
        square.update(x=2, y=3, id=123)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 123)

    def test_to_dictionary(self):
        square = Square(10, x=2, y=3, id=123)
        expected_dict = {"id": 123, "size": 10, "x": 2, "y": 3}
        self.assertEqual(square.to_dictionary(), expected_dict)
