#!usr/bin/python3
""" My file storage module """


class FileStorage:
    """ The file storage class """
    __file_path = "file.json"

    #  will store all objects by <class name>.id (ex: to store a BaseModel
    #  object with id=12121212, the key will be BaseModel.12121212)
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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        pass

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        """
        pass
