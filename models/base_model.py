#!/usr/bin/python3
"""
This modules Defines the base class model
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """ the base model to create objects in our app"""

    def __init__(self, *args, **kwargs):
        """initiamizes the BaseModel class
        Args:
            *args.
            **kwargs(dict) key/value
        representation of a class'attr
        """
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, d_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the public instance\
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.today()
        models.storage.new(self)

    def to_dict(self):
        """returns a dictionary\
        containing all keys/values of __dict__ of the instanc"""
        tmp = self.__dict__.copy()
        tmp["created_at"] = self.created_at.isoformat()
        tmp["updated_at"] = self.updated_at.isoformat()
        tmp["__class__"] = self.__class__.__name__
        return tmp

    def __str__(self):
        """
        Returns the official\
        representation of\
        the base model object
        """
        return("[{}] ({}) {}".format(
                   self.__class__.__name__,
                   self.__str__(),
                   self.__dict__))
