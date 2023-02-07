#!/usr/bin/python3
""" Defines the base class model"""

import uuid
import datetime

class BaseModel():
    """ the base model to create objects in our app"""
    id = ""
    created_at = None
    updated_at = None

    def __init__(self):
        """initiamizes the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instanc"""
        dico = self.__dict__
        dico['__class__'] = self.__class__.__name__
        return(dico)

    def __str__(self):
        """ Returns the official representation of the base model object"""
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
    
