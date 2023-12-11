#!/usr/bin/python3
"""Unittest for City class
"""
import unittest
from models.city import City


class testCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Create City instance for tests"""
        self.city = City()

    def tearDown(self):
        """Destroy City instance after tests"""
        del self.city

    def testCityClassPublicAttributes(self):
        """Test if City class have public attributes"""
        self.assertNotIn('state_id', self.city.__dict__)
        self.assertIn('state_id', City.__dict__)
        self.assertEqual(City.state_id, '')
        self.assertIs(type(City.state_id), str)

        self.assertNotIn('name', self.city.__dict__)
        self.assertIn('name', City.__dict__)
        self.assertEqual(City.name, '')
        self.assertIs(type(City.name), str)
