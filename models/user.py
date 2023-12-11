#!/usr/bin/python3
""" User module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Define a user.

    :param email: user's email
    :type email: str
    :param password: user's password
    :type password: str
    :param first_name: user's first name
    :type first_name: str
    :param last_name: user's last name
    :type last_name: str
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
