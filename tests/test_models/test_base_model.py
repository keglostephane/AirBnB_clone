#!/usr/bin/python3
"""Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel
from io import StringIO
from datetime import datetime
from unittest.mock import patch


class testBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Create BaseModel instance for tests"""
        self.model = BaseModel()

    def tearDown(self):
        """Destroy BaseModel instance after tests"""
        del self.model

    def testBaseModelInstanceAttributes(self):
        """Test if attributes of an BaseModel instance exists."""
        self.assertIn('id', self.model.__dict__)
        self.assertIn('created_at', self.model.__dict__)
        self.assertIn('updated_at', self.model.__dict__)

    def testBaseModelInstanceAttributesType(self):
        """Test BaseModel instance attributes type."""
        self.assertTrue(type(self.model.id), str)
        self.assertTrue(type(self.model.created_at), datetime)
        self.assertTrue(type(self.model.updated_at), datetime)

    def testBaseModelInstanceStringRepresentation(self):
        """Test BaseModel instance human readable representation."""
        with patch('sys.stdout', new_callable=StringIO) as output:
            self.model.id = '99e76600-5dab-46bb-a46c-0af91a7400b7'
            self.model.created_at = datetime(2023, 12, 5, 19, 28, 12, 717461)
            self.model.updated_at = datetime(2023, 12, 5, 19, 29, 47, 135265)
            self.model.name = 'model'
            print(self.model)
            result = output.getvalue()
            expected = ("[BaseModel] (99e76600-5dab-46bb-a46c-0af91a7400b7) "
                        "{'id': '99e76600-5dab-46bb-a46c-0af91a7400b7', "
                        "'created_at': "
                        "datetime.datetime(2023, 12, 5, 19, 28, 12, 717461), "
                        "'updated_at': "
                        "datetime.datetime(2023, 12, 5, 19, 29, 47, 135265), "
                        "'name': 'model'}\n")
        self.assertEqual(result, expected)

    def testBaseModelSave(self):
        """Test BaseModel save() method."""
        date = self.model.updated_at
        self.model.save()
        self.assertNotEqual(date, self.model.updated_at)

    def testBaseModelToDict(self):
        """Test BaseModel to_dict() method."""
        self.model.id = '5c738bb0-6bc5-4c91-a49e-fb57b946abd8'
        self.model.created_at = datetime(2023, 12, 5, 20, 26, 18, 554069)
        self.model.updated_at = datetime(2023, 12, 5, 20, 28, 9, 800791)
        self.model.name = 'model'
        result = self.model.to_dict()
        expected = {'id': '5c738bb0-6bc5-4c91-a49e-fb57b946abd8',
                    '__class__': 'BaseModel',
                    'created_at': '2023-12-05T20:26:18.554069',
                    'updated_at': '2023-12-05T20:28:09.800791',
                    'name': 'model'}
        self.assertEqual(result, expected)
