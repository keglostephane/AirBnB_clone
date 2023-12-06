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
