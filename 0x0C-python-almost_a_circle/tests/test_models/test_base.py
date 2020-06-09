#!/usr/bin/python3
"""
creating class basetest
"""
import unittest
from models.base import Base


class basetest(unittest.TestCase):
    """
    testing class Base
    """
    def test_arguments(self):
        """
        testing id
        """
        base = Base()
        self.assertEqual(base.id, 1)

    def test_none(self):
        """
        id as None
        """
        base = Base(None)
        self.assertEqual(base.id, 2)

    def test_mult(self):
        """
        multiple
        """
        base1 = Base(1)
        base2 = Base(2)
        base3 = Base(3)
        base4 = Base(4)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
        self.assertEqual(base4.id, 4)

    def test_same_id(self):
        """
        two bases with same id
        """
        b1 = Base(1)
        b2 = Base(1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1)

if __name__ == '__main__':
    unittest.main()