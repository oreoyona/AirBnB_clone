#!/usr/bin/python3
"""This modules contains tests cases using
pythln unittest module for the FileStorage class
"""

import inspect
import json
import os
import unittest
import pycodestyle
from models.engine import file_storage
from tests.test_models.test_base_model import BaseModel

FileStorage = file_storage.FileStorage


class TestPycldeStyle(unittest.TestCase):
    """Tests FileStorage class for documentation and style"""

    def test_pycodestyle(self):
        """Test the pycodestyle adherence"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            [
                "models/engine/file_storage.py",
                "tests/test_models/test_engine/test_file_storage.py"
            ])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests the documentation of our module""
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests the documentation of our class"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the memebers
        are documented"""
        funcs = inspect.getmembers(FileStorage, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

class TestFileStorage(unittest.TestCase):
    """Tests the FileStorage Class"""

    def setUp(self):
        """initialization of the class"""
        self.file_path = "file.json"
        with open(self.file_path, 'w') as f:
            json.dump({}, f)
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """cleanup test files"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_dico(self):
        """tests the return_type of a method
        returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_addOp(self):
        """tests wether the instance method
        creates a new _object"""
        temp = BaseModel()
        self.storage.new(temp)
        key = f"{temp.__class__.__name__}.{temp.id}"
        self.assertIn(key, self.storage.all().keys())

    def test_storing(self):
        """tests wether the save method saves objects"""
        tmp = {}
        for _ in range(4):
            bs_mdl = BaseModel()
            self.storage.new(bs_mdl)
            key = f"{bs_mdl.__class__.__name__}.{bs_mdl.id}"
           tmp[key] = bs_mdl.to_dict()

        self.storage.save()

        self.assertTrue(os.path.exists(self.file_path))
        self.assertGreater(os.path.getsize(self.file_path), 0)
        with open(self.file_path, 'r') as f:
            objects = {k: v
                       for k, v in json.load(f).items()}

        self.assertDictEqual(tmp, objects)

    def test_memory(self):
        """tests wether the _reload method
        loads objects"""
        tmp = {}
        for _ in range(4):
            bs_mdl = BaseModel()
            self.storage.new(bs_mdl)
            key = f"{bs_mdl.__class__.__name__}.{bs_mdl.id}"
           tmp[key] = bs_mdl.to_dict()

        self.storage.save()
        self.storage.reload()
        data = self.storage.all()

        data_obj = {k: v.to_dict() for k, v in data.items()}
        self.assertEqual(tmp, data_obj)
