#!/usr/bin/python3
""" FileStorage module
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Define all common attributes and methods for child classes.

    :param __file_path: path to the JSON file
    :type __file_path: str
    :param __objects: dictionary that will store all objects
    :type __objects: str
    """
    __file_path = 'file.json'
    __objects = {}

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
                elif cls_name == "User":
                    self.__objects[key] = User(**value)
                elif cls_name == "State":
                    self.__objects[key] = State(**value)
                elif cls_name == "City":
                    self.__objects[key] = City(**value)
                elif cls_name == "Amenity":
                    self.__objects[key] = Amenity(**value)
                elif cls_name == "Place":
                    self.__objects[key] = Place(**value)
                elif cls_name == "Review":
                    self.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
