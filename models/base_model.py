#!/usr/bin/python3
"""
This modules Defines the base class model
"""

import uuid
import datetime
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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k in ["created_at", "updated_at"]:
                    setattr(self, k, datetime.datetime.fromisoformat(v))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """
        updates the public instance\
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def to_dict(self):
        """returns a dictionary\
        containing all keys/values of __dict__ of the instanc"""
        tmp = (
            {
                k: (v.isoformat() if isinstance(v, datetime.datetime) else v)
                for (k, v) in self.__dict__.items()
            }
        )
        tmp["__class__"] = self.__class__.__name__
        return tmp

    def __str__(self):
        """
        Returns the official\
        representation of\
        the base model object
        """
        return("[{}] ({}) {}".format
               (
                   self.__class__.__name__,
                   self.__str__(),
                   self.__dict__))
