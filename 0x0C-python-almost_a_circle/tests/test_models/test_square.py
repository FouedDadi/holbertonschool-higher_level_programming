#!/usr/bin/python3
"""
creating class Square
"""
import unittest
from models.square import Square


class testSquare(unittest.TestCase):
    """
    testing class Sqaure
    """
    def test_typeerror(self):
        """
        testing type error
        """
        with self.assertRaises(TypeError):
            Square("hey", "hello")

    def test_valueerror(self):
        """
        testing value error
        """
        with self.assertRaises(ValueError):
            Square(-5, -9)

if __name__ == '__main__':
    unittest.main()