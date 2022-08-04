#!/usr/bin/python3
""" Base Model class for the entities in the Airbnb Project """
import uuid
import datetime

class BaseModel:
    """The BaseModel Class"""
    def __init__(self):
        """The initializer for the BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """the string representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance """
        dict_format = self.__dict__
        dict_format["__class__"] = self.__class__.__name__
        return dict_format
