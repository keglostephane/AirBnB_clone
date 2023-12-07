#!/usr/bin/python3
""" City module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel

    :param place_id: id of the place
    :type place_id: str
    :param user_id: id of the user
    :type user_id: str
    :param text: text
    :type text: str
    """
    place_id = ""
    user_id = ""
    text = ""
