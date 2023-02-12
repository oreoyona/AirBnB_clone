#!/usr/bin/python3
"""This modules the file storage class"""


import importlib
import json
import os
import re


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns __objects"""
        return self.__objects

    def new(self, obj):
        """Setter of the private member  __objects"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Saves the member __objects
        to the JSON file __file_path."""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Converts the JSON file
        to __objects, if it exists."""
        if (os.path.isfile(self.__file_path)
                and os.path.getsize(self.__file_path) > 0):
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: self.get_class(k.split(".")[0])(**v)
                                  for k, v in json.load(f).items()}

    def get_class(self, name):
        """A class getter from models packagee"""
        sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
        module = importlib.import_module(f"models.{sub_module}")
        return getattr(module, name)
