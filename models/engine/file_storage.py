#!/usr/bin/python3
"""Module for FileStorage class."""


import re
import importlib
import json
import os


class FileStorage:
    """Defines the FileStorage class
    Attributes:
        __file_path (str):The path to the JSON file
        __objects (dict): A dictionary of objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Gets all the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates an object with a new ID"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Saves the JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Reloads the JSON file"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
