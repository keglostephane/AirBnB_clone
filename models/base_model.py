#!/usr/bin/python3
"""A BaseModel module
"""
import json
import uuid
from datetime import datetime


class BaseModel:
    """Define all common attributes and methods for child classes.

    :param id: unique identifier
    :type id: str
    :param created_at: creation date
    :type created_at: str
    :param updated_at: last modification date
    :type updated_at: str
    """

    def __init__(self):
        """Initializer"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Human readable representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the last modification date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict.update(created_at=self.created_at.isoformat())
        new_dict.update(updated_at=self.updated_at.isoformat())
        new_dict.update(__class__=self.__class__.__name__)
        return new_dict
