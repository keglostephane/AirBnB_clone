#!/usr/bin/python3
""" City module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel

    :param state_id: State
    :type state_id: str
    :param name: name of the city
    :type name: str
    """
    state_id = ""
    name = ""
