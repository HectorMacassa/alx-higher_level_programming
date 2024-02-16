#!/usr/bin/python3

"""
Unit Tests for square.py
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test suite for the Square class.
    """

    def test_constructor(self):
        """
        Test the constructor method of the Square class.
        """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

        s2 = Square(10, 2, 3, 20)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 20)

    def test_update(self):
        """
        Test the update method of the Square class.
        """
        s = Square(5)
        s.update(1)
        self.assertEqual(s.id, 1)
        s.update(1, 10)
        self.assertEqual(s.size, 10)
        s.update(1, 10, 2, 3)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_str_representation(self):
        """
        Test the __str__ method of the Square class.
        """
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

        with self.assertRaises(ValueError):
            s = Square(-5, 2, 3, 1)
            s.to_dictionary()

        with self.assertRaises(ValueError):
            s = Square(5, -2, 3, 1)
            s.to_dictionary()

        with self.assertRaises(ValueError):
            s = Square(5, 2, -3, 1)
            s.to_dictionary()

        with self.assertRaises(TypeError):
            s = Square("5", 2, 3, 1)
            s.to_dictionary()

        with self.assertRaises(TypeError):
            s = Square(5, "2", 3, 1)
            s.to_dictionary()

        with self.assertRaises(TypeError):
            s = Square(5, 2, "3", 1)
            s.to_dictionary()


if __name__ == '__main__':
    unittest.main()
