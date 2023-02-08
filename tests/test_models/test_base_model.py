#!/usr/bin/python3
"""
This modules contains all the Tests
it tests cases for the BaseModel class
"""


import unittest
import inspect
from models import base_model as bm


class TestCodeStyle(unittest.TestCase):
    """
    Tests wether the base class
    is written correctly
    """

    def test_pycodestyle(self):
        """Tests if the class passes pycodestyle"""

        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/base_model.py", "tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(BaseModel, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(BaseModel.__name__, "BaseModel")


class BaseModelTest(unittest.TestCase):
    """ Tests the BaseModel class"""
    gloire = bm.BaseModel()

    def test_isDaughter(self):
        """Tests wether a given class is an instance ofthe BaseModel class"""
        print(self.gloire.__str__())
        self.assertIsInstance(
            self.gloire,
            bm.BaseModel,
            "Is not an instance of the BaseModel class")
            
if __name__ == "__main__":
    unittest.main()
