#!/usr/bin/python3
"""
creating class rectangle
"""
import unittest
from models.rectangle import Rectangle


class testRectangle(unittest.TestCase):
    """
    testing class rectangle
    """
    def test_typeerror(self):
        """
        testing type error
        """
        with self.assertRaises(TypeError):
            Rectangle("hey", "hello")

    def test_valueerror(self):
        """
        testing value error
        """
        with self.assertRaises(ValueError):
            Rectangle(-5, -9)

if __name__ == '__main__':
    unittest.main()