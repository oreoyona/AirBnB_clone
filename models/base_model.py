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
        self.id = str(uuid.uuidr4())
        self.created_at = datetime.datetime
        self.updated_at = datetime.datetime
    
