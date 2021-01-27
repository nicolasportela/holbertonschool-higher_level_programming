#!/usr/bin/python3
import unittest
import inspect
import json


from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """Tests to check the documentation and style of Base class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_id(self):
        """Tests id as None"""
        b = Base()
        self.assertEqual(b.id, 2)

    def test_id_set(self):
        """Tests id as not None"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_no_id_after_set(self):
        """Tests id as None after not None"""
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_None_id(self):
        """Tests id as None after not None"""
        bN = Base(None)
        self.assertEqual(bN.id, 1)

    def test_too_many_args(self):
        """Tests too many args to init"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_to_json_string(self):
        """Tests regular to json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def test_empty_to_json_string(self):
        """Test for passing empty list"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_None_to_json_String(self):
        """Test for passing None"""
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Tests regular from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
                        {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def test_fjs_None(self):
        """Tests from_json_string with None"""
        self.assertEqual([], Base.from_json_string(None))