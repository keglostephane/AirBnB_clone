#!/usr/bin/python3
"""Unittest for FileStorage class
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Create FileStorage instance for tests"""
        self.storage = FileStorage()

    def tearDown(self):
        """Destroy FileStorage instance after tests"""
        del self.storage

    def testFileStorageClassPrivateAttributes(self):
        """Test if FileStorage class have __file_path private attributes
        """
        self.assertNotIn('_FileStorage__file_path', self.storage.__dict__)
        self.assertNotIn('_Filestorage__ojects', self.storage.__dict__)
        self.assertEqual({}, self.storage.__dict__)
        self.assertIs(type(self.storage._FileStorage__file_path), str)
        self.assertIs(type(self.storage._FileStorage__objects), dict)
        self.assertEqual(self.storage._FileStorage__file_path, 'file.json')

    def testFileStorageAll(self):
        """Test FileStorage instance all() method"""
        self.assertIs(type(self.storage.all()), dict)
        self.assertEqual(self.storage.all(),
                         self.storage._FileStorage__objects)
        self.assertIs(self.storage.all(),
                      self.storage._FileStorage__objects)

    def testFileStorageNew(self):
        """Test FileStorage instance new() method"""
        objects_dict = self.storage.all()
        model = BaseModel()
        key = f"{model.__class__.__name__}.{model.id}"
        self.storage.new(model)
        self.assertEqual(objects_dict, self.storage._FileStorage__objects)
        self.assertIn(key, objects_dict.keys())
        self.assertEqual(objects_dict[key], model)

    def testFileStorageSave(self):
        """Test FileStorage instance save() method"""
        # tests if objects are saved to file.json
        filename = 'file.json'
        if os.path.exists(filename):
            os.remove(filename)
        self.storage.save()
        self.assertTrue(os.path.exists(filename))

        # deserialize objects saved to file.json and compare with
        # original dict of objects
        with open(filename, encoding='utf-8') as json_file:
            json_dict_objects = json.load(json_file)

        dict_objects = {key: value.to_dict() for key, value
                        in self.storage.all().items()}

        self.assertEqual(dict_objects, json_dict_objects)

    def testFileStorageReload(self):
        """Test FileStorage instance reload() method"""
        # json file already exits
        filename = 'file.json'
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertNotEqual(self.storage.all(), {})

        # json file doesn't exists
        if os.path.exists(filename):
            os.remove(filename)
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def testFileStorageUniqueInstance(self):
        """Test if Filestorage class has already an instance"""
        from models import storage
        self.assertIsInstance(storage, FileStorage)
        self.assertNotEqual(storage._FileStorage__objects, {})
