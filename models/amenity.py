#!/usr/bin/python3
""" Amenity module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel

    :param name: name
    :type name: str
    """
    name = ""
