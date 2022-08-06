#!usr/bin/python3
""" My file storage module """
import json
import os
from pathlib import Path


BASE_DIR = Path(os.getcwd()).resolve()


class FileStorage:
    """ The file storage class """
    __file_path = BASE_DIR / "file.json"
    __objects = {}

    def __init__(self):
        """Initialization method"""
        pass

    def all(self):
        """ Returns all of the objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ Sets a new object to the object dict """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        save_dict = {}
        if FileStorage.__objects:
            for key, value in FileStorage.__objects.items():
                save_dict[key] = value.to_dict()

            with open(FileStorage.__file_path, "w") as f:
                json.dump(save_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        """
        if FileStorage.__file_path.exists():
            with open(FileStorage.__file_path, "r") as r:
                reload_dict = json.load(r)

                if reload_dict:
                    from models.base_model import BaseModel
                    FileStorage.__objects = {}
                    for key, value in reload_dict.items():
                        FileStorage.__objects[key] = BaseModel(**value)
