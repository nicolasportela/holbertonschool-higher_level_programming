#!/usr/bin/python3
"""Module test for the Square class"""

import unittest
import inspect
import json
from models import square
from models.base import Base
Square = square.Square


class TestSquareDocs(unittest.TestCase):
    """Tests the Square class' style and documentation"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.sq_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for the presence of a module docstring"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    class TestSquare(unittest.TestCase):
        """Test the functionality of the Square class"""
    @classmethod
    def setUpClass(cls):
        """set up the tests"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)

    def test_id(self):
        """Test for functioning ID"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)

    def test_size(self):
        """Test for functioning size"""
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 2)

    def test_x(self):
        """Test for functioning x"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 3)

    def test_y(self):
        """Test for functioning y"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)

    def test_size_typeerror(self):
        """Test non-ints for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")

    def test_size_valueerror(self):
        """Test ints <= 0 for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_area(self):
        """test area"""
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 4)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            a = self.s1.area(1)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.s1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.s2), "[Square] (2) 3/0 - 2")

    def test_update_args(self):
        """Testing the udpate method with *args"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/0 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_args_setter(self):
        """tests that the update method uses setter with *args"""
        s = Square(1, 0, 0, 1)
        with self.assertRaises(TypeError):
            s.update(1, "hello")
        with self.assertRaises(TypeError):
            s.update(1, 1, "hello")
        with self.assertRaises(TypeError):
            s.update(1, 1, 1, "hello")
        with self.assertRaises(ValueError):
            s.update(1, 0)
        with self.assertRaises(ValueError):
            s.update(1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, -1)
        with self.assertRaises(ValueError):
            s.update(1, 1, 1, -1)

    def test_update_no_args(self):
        """test no args for update"""
        s = Square(1, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")

    def test_update_kwargs(self):
        """Testing the update method with **kwargs"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=10)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        s.update(size=11, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 11")
        s.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(s), "[Square] (89) 5/3 - 4")

    def test_update_kwargs_setter(self):
        """tests that the update method uses setter with **kwargs"""
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.update(size="hello")
        with self.assertRaises(TypeError):
            s.update(x="hello")
        with self.assertRaises(TypeError):
            s.update(y="hello")
        with self.assertRaises(ValueError):
            s.update(size=-1)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-1)
        with self.assertRaises(ValueError):
            s.update(y=-1)

    def test_to_dict(self):
        """test regular to_dictionary"""
        d1 = self.s1.to_dictionary()
        self.assertEqual({"id": 1, "size": 1, "x": 0, "y": 0}, d1)
        d2 = self.s2.to_dictionary()
        self.assertEqual({"id": 2, "size": 2, "x": 3, "y": 0}, d2)
        self.assertTrue(type(d1) is dict)
        self.assertTrue(type(d2) is dict)

    def test_save_to_file(self):
        """test regular use of save_to_file"""
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        l = [s1, s2]
        Square.save_to_file(l)
        with open("Square.json", "r") as f:
            ls = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(json.dumps(ls), f.read())

    def test_create(self):
        """test normal use of create"""
        s1 = {"id": 2, "size": 3, "x": 4, "y": 0}
        s2 = {"id": 9, "size": 6, "x": 7, "y": 8}
        s1c = Square.create(**s1)
        s2c = Square.create(**s2)
        self.assertEqual("[Square] (2) 4/0 - 3", str(s1c))
        self.assertEqual("[Square] (9) 7/8 - 6", str(s2c))
        self.assertNotEqual(s1, s1c)
        self.assertNotEqual(s2, s2c)