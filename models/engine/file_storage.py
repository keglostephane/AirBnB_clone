#!/usr/bin/python3
""" FileStorage module
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Define all common attributes and methods for child classes.

    :param __file_path: path to the JSON file
    :type __file_path: str
    :param __objects: dictionary that will store all objects
    :type __objects: str
    """
    def __init__(self):
        """ initializer """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ retrieve all objects """
        return self.__objects

    def new(self, obj):
        """ a new object in __objects dict """
        key = f"{ obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes objects to the Json file """
        with open(self.__file_path, 'w') as fp:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, fp)

    def reload(self):
        """ deserializes the Json file to _objects """
        try:
            with open(self.__file_path, 'r') as fp:
                objects = json.load(fp)
                for key, value in objects.items():
                    cls_name, object_id = key.split(".")
                    if cls_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
