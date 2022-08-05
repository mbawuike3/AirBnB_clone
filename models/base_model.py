#!/usr/bin/python3
""" Base Model class for the entities in the Airbnb Project """
import uuid
import datetime
from models import storage


class BaseModel:
    """The BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """The initializer for the BaseModel class"""
        """
        {'id': '6c3e950d-1fa7-416e-83c4-189215c39282', 
        'created_at': '2022-08-04T18:48:40.217062', 
        'updated_at': '2022-08-04T18:48:40.217115', 
        'name': 'My First Model', 'my_number': 89, '__class__': 'BaseModel'}
        """
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'name' in kwargs:
                self.name = kwargs['name']
            if 'my_number' in kwargs:
                self.my_number = kwargs['my_number']
            if 'created_at' in kwargs:
                self.created_at = datetime.datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs:
                self.updated_at = datetime.datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """the string representation of an object"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        storage.save()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dict_format = self.__dict__
        dict_format["__class__"] = self.__class__.__name__
        dict_format["created_at"] = dict_format["created_at"]\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict_format["updated_at"] = dict_format["updated_at"]\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dict_format
