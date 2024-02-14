#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init(self):
        # Test valid initialization
        rect = Rectangle(10, 5)
        self.assertEqual(rect.id, Base.get_id())
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

        # Test initialization with specific x and y
        rect_xy = Rectangle(10, 5, x=2, y=3)
        self.assertEqual(rect_xy.x, 2)
        self.assertEqual(rect_xy.y, 3)

        # Test initialization with id
        rect_id = Rectangle(10, 5, id=123)
        self.assertEqual(rect_id.id, 123)

    def test_invalid_init(self):
        # Test invalid width (not int)
        with self.assertRaises(TypeError):
            Rectangle("invalid", 5)

        # Test invalid width (less than or equal to 0)
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

        # Test invalid height (not int)
        with self.assertRaises(TypeError):
            Rectangle(10, "invalid")

        # Test invalid height (less than or equal to 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

        # Test invalid x (not int)
        with self.assertRaises(TypeError):
            Rectangle(10, 5, x="invalid")

        # Test invalid x (negative)
        with self.assertRaises(ValueError):
            Rectangle(10, 5, x=-1)

        # Test invalid y (not int)
        with self.assertRaises(TypeError):
            Rectangle(10, 5, y="invalid")

        # Test invalid y (negative)
        with self.assertRaises(ValueError):
            Rectangle(10, 5, y=-1)

    def test_width_setter(self):
        rect = Rectangle(10, 5)

        # Test valid setter
        rect.width = 15
        self.assertEqual(rect.width, 15)

        # Test invalid setter (not int)
        with self.assertRaises(TypeError):
            rect.width = "invalid"

        # Test invalid setter (less than or equal to 0)
        with self.assertRaises(ValueError):
            rect.width = 0

    def test_height_setter(self):
        rect = Rectangle(10, 5)

        # Test valid setter
        rect.height = 8
        self.assertEqual(rect.height, 8)

        # Test invalid setter (not int)
        with self.assertRaises(TypeError):
            rect.height = "invalid"

        # Test invalid setter (less than or equal to 0)
        with self.assertRaises(ValueError):
            rect.height = 0

    def test_x_setter(self):
        rect = Rectangle(10, 5)

        # Test valid setter
        rect.x = 3
        self.assertEqual(rect.x, 3)

        # Test invalid setter (not int)
        with self.assertRaises(TypeError):
            rect.x = "invalid"

        # Test invalid setter (negative)
        with self.assertRaises(ValueError):
            rect.x = -1

    def test_y_setter(self):
        rect = Rectangle(10, 5)

        # Test valid setter
        rect.y = 4
        self.assertEqual(rect.y, 4)

        # Test invalid setter (not int)
        with self.assertRaises(TypeError):
            rect.y = "invalid"

        # Test invalid setter (negative)
        with self.assertRaises(ValueError):
            rect.y = -1

    def test_area(self):
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        # Capturing output to compare
        with self.assertRaises(NotImplementedError):
            rect = Rectangle(10, 5)
            rect.
