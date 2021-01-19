#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """List of tests"""
    def test_ints(self):
        """test with a list of ints"""
        self.assertEqual(max_integer([1, 2, 8, 4]), 8)

    def test_beg(self):
        """test for max at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_end(self):
        """test for max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4], 4)

    def test_one(self):
        """test for list of one element"""
        self.assertEqual(max_integer([4], 4)

    def test_empty(self):
        """test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_char(self):
        """test a list of chars(ASCII)"""
        self.assertEqual(max_integer(["a", "C", "c", "b"]), "c")

    def test_not_list(self):
        """testing int as argument"""
        with self.assertRaises(TypeError):
            max_integer(13)

    def test_none(self):
        """testing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
