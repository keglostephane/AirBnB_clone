#!/usr/bin/python3
"""Unittest for BaseModel class
"""
import unittest
import json
from models.base_model import BaseModel
from models import storage
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
        self.assertIs(type(self.model.id), str)
        self.assertIs(type(self.model.created_at), datetime)
        self.assertIs(type(self.model.updated_at), datetime)

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
        self.assertIs(type(self.model.to_dict()), dict)

    def testBaseModelInit(self):
        """Test BaseModel instance initialization."""
        id = '6262702c-96c8-4532-8d74-e977a61a90c9'
        created = datetime(2023, 12, 6, 21, 25, 48, 820626)
        updated = datetime(2023, 12, 6, 21, 25, 50, 820621)
        name = 'model_1'

        # only positional arguments
        model_1 = BaseModel(id, created, updated, name)
        self.assertNotEqual(model_1.id, id)
        self.assertNotEqual(model_1.created_at, created)
        self.assertNotEqual(model_1.updated_at, updated)
        self.assertNotIn('name', model_1.__dict__)

        # only keyword arguments
        model_2 = BaseModel(id=id, created_at=created.isoformat(),
                            updated_at=updated.isoformat(),
                            name='model_2', __class__='Base')
        self.assertEqual(model_2.id, id)
        self.assertEqual(model_2.created_at, created)
        self.assertIs(type(model_2.created_at), datetime)
        self.assertIs(type(model_2.updated_at), datetime)
        self.assertEqual(model_2.updated_at, updated)
        self.assertEqual(model_2.name, 'model_2')
        self.assertNotIn('__class__', model_2.__dict__)

        # positional and keyword arguments
        model_3 = BaseModel(id, created, updated_at=updated.isoformat(),
                            name='model_3')
        self.assertNotIn('id', model_3.__dict__)
        self.assertNotIn('created_at', model_3.__dict__)
        self.assertIn('updated_at', model_3.__dict__)
        self.assertIn('name', model_3.__dict__)

        # invalid date,time format
        self.assertRaises(TypeError, BaseModel,
                          created_at=created,
                          updated_at=updated)

        with self.assertRaises(ValueError) as error:
            BaseModel(created_at='2023-12-06')
            self.assertEqual(error.exception,
                             ("time data '2023-12-06' does not match "
                              "format '%Y-%m-%dT%H:%M:%S.%f'"))
        with self.assertRaises(ValueError) as error:
            BaseModel(created_at='2023-12-06 21')
            self.assertEqual(error.exception,
                             ("time data '2023-12-06 21' does not match "
                              "format '%Y-%m-%dT%H:%M:%S.%f'"))
        with self.assertRaises(ValueError) as error:
            BaseModel(created_at='2023-12-06T21:30:15')
            self.assertEqual(error.exception,
                             ("time data '2023-12-06T21:30:15' does not match "
                              "format '%Y-%m-%dT%H:%M:%S.%f'"))

        # correct date,time format
        model_4 = BaseModel(created_at='2023-06-08T09:12:30.5')
        self.assertIn('created_at', model_4.__dict__)
        self.assertIs(type(model_4.created_at), datetime)
        self.assertEqual(model_4.created_at,
                         datetime(2023, 6, 8, 9, 12, 30, 500000))

        # recreate a BaseModel object from a dictionary
        model_dict = self.model.to_dict()
        model_5 = BaseModel(**model_dict)
        self.assertEqual(model_5.to_dict(), model_dict)
        self.assertIsNot(model_5, self.model)

    def testBaseModelLinkToFileStorage(self):
        """Test the linking of BaseModel to FileStorage"""
        # test if BaseModel instances not created from a dictionary
        # representation are added to storage list of objects
        model_1 = BaseModel(created_at='2022-05-21T17:12:05.12',
                            name='model_1')
        model_2 = BaseModel()
        self.assertIn(model_2, storage.all().values())
        self.assertNotIn(model_1, storage.all().values())

        # test if BaseModel instances save() method save to json file
        filename = 'file.json'
        model_3 = BaseModel()
        model_3.save()
        with open(filename, encoding='utf-8') as json_file:
            json_dict_objects = json.load(json_file)
        self.assertIn(model_3.to_dict(), json_dict_objects.values())
