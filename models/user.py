#!/usr/bin/python3
""" User module
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Define all common attributes and methods for child classes.

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

    def __init__(self, *args, **kwargs):
        """Initializer"""
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
            self.first_name = User.first_name
            self.last_name = User.last_name
            self.email = User.email
            self.password = User.password
            models.storage.new(self)
