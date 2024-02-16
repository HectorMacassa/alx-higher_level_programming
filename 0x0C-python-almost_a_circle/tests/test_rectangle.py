#!/usr/bin/python3

"""
Unit Tests for rectangle.py
"""

import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test suite for the Rectangle class
    """

    def test_constructor(self):
        """
        Test constructor method
        """
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertIsNotNone(r1.id)

        r2 = Rectangle(15, 25, 5, 8, 300)
        self.assertEqual(r2.width, 15)
        self.assertEqual(r2.height, 25)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 8)
        self.assertEqual(r2.id, 300)

    def test_id_assignment(self):
        """
        Test if id is being assigned properly
        """
        r1 = Rectangle(10, 20)
        r2 = Rectangle(5, 15)
        r3 = Rectangle(8, 12)

        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r2.id, r3.id - 1)

    def test_attribute_validations(self):
        """
        Test attribute validations
        """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 25)
        with self.assertRaises(ValueError):
            r = Rectangle(30, 0)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20)
        with self.assertRaises(ValueError):
            r = Rectangle(20, -30)
        with self.assertRaises(TypeError):
            r = Rectangle("20", 10)
        with self.assertRaises(TypeError):
            r = Rectangle(20, "10")

        with self.assertRaises(ValueError):
            r = Rectangle(20, 30, -5, 10)
        with self.assertRaises(ValueError):
            r = Rectangle(20, 30, 5, -10)
        with self.assertRaises(TypeError):
            r = Rectangle(20, 30, "5", 10)
        with self.assertRaises(TypeError):
            r = Rectangle(20, 30, 5, "10")

    def test_area(self):
        """
        Test area method
        """
        r = Rectangle(8, 6)
        self.assertEqual(r.area(), 48)

        r2 = Rectangle(10, 10)
        self.assertEqual(r2.area(), 100)

    def test_display(self):
        """
        Test display method
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output

        r = Rectangle(4, 3)
        r.display()
        sys.stdout = sys.__stdout__

        expected_output = "####\n####\n####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

        captured_output = io.StringIO()
        sys.stdout = captured_output

        r2 = Rectangle(5, 5)
        r2.display()
        sys.stdout = sys.__stdout__

        expected_output = "#####\n#####\n#####\n#####\n#####\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_string_representation(self):
        """
        Test string representation method
        """
        r = Rectangle(6, 9, 2, 3, 300)
        expected_output = "[Rectangle] (300) 2/3 - 6/9"
        actual_output = str(r)
        self.assertEqual(actual_output, expected_output)

        r2 = Rectangle(8, 12, 1, 1, 56)
        expected_output2 = "[Rectangle] (56) 1/1 - 8/12"
        actual_output2 = str(r2)
        self.assertEqual(actual_output2, expected_output2)

    def test_multiple_display(self):
        """
        Test display method with multiple rectangles
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output

        r1 = Rectangle(2, 2)
        r2 = Rectangle(3, 3, 1, 1)
        r1.display()
        print("\n")
        r2.display()
        sys.stdout = sys.__stdout__

        expected_output = "##\n##\n\n\n\n ###\n ###\n ###\n"
        actual_output = captured_output.getvalue()
        self.assertEqual(actual_output, expected_output)

    def test_update(self):
        """
        Test update method
        """
        r = Rectangle(3, 4)
        r.update(5)
        self.assertEqual(r.id, 5)
        r.update(5, 6)
        self.assertEqual(r.width, 6)
        r.update(5, 6, 7)
        self.assertEqual(r.height, 7)
        r.update(5, 6, 7, 8)
        self.assertEqual(r.x, 8)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(r.y, 9)

        r.update(6, 7, 8, 9, 10)
        self.assertEqual(r.id, 6)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

    def test_update_with_kwargs(self):
        """
        Test update method with keyword arguments
        """
        r = Rectangle(3, 4)
        r.update(width=5)
        self.assertEqual(r.width, 5)
        r.update(height=6)
        self.assertEqual(r.height, 6)
        r.update(x=7)
        self.assertEqual(r.x, 7)
        r.update(y=8)
        self.assertEqual(r.y, 8)
        r.update(id=9)
        self.assertEqual(r.id, 9)
        r.update(id=10, width=11, height=12, x=13, y=14)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 11)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 13)
        self.assertEqual(r.y, 14)

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 10, 'height': 20, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20, 2, 3, 1)
            r.to_dictionary()

        with self.assertRaises(ValueError):
            r = Rectangle(10, -20, 2, 3, 1)
            r.to_dictionary()

        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -2, 3, 1)
            r.to_dictionary()

        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 2, -3, 1)
            r.to_dictionary()

        with self.assertRaises(TypeError):
            r = Rectangle("10", 20, 2, 3, 1)
            r.to_dictionary()

        with self.assertRaises(TypeError):
            r = Rectangle(10, "20", 2, 3, 1)
            r.to_dictionary()

        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "2", 3, 1)
            r.to_dictionary()

        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 2, "3", 1)
            r.to_dictionary()


if __name__ == '__main__':
    unittest.main()
