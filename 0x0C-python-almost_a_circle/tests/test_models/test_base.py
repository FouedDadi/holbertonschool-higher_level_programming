#!/usr/bin/python3
import unittest
from models.base import Base
"""
creating class basetest
"""
class basetest(unittest.TestCase):
    """
    testing class Base
    """
    def test_arguments(self):
        """
        testing id
        """
        base = Base()
        self.assertEqual(base.id, 12)

if __name__ == '__main__':
    unittest.main()