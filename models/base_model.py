#!/usr/bin/python3
"""A BaseModel module
"""
import models
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

    def __init__(self, *args, **kwargs):
        """Initializer"""
        if kwargs:
            for attr, value in kwargs.items():
                if attr != "__class__":
                    if attr in ["created_at", "updated_at"]:
                        dformat = "%Y-%m-%dT%H:%M:%S.%f"
                        setattr(self, attr, datetime.strptime(value, dformat))
                    else:
                        setattr(self, attr, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Human readable representation"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the last modification date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        new_dict.update(created_at=self.created_at.isoformat())
        new_dict.update(updated_at=self.updated_at.isoformat())
        new_dict.update(__class__=self.__class__.__name__)
        return new_dict
