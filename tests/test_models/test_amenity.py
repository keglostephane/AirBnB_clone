#!/usr/bin/bin/python3
"""Unittest for User class
"""
import unittest
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Create Amenity instance for tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Destroy Amenity instance after tests"""
        del self.amenity

    def testAmenityClassPublicAttribute(self):
        """Test if Amenity class have public attributes"""
        self.assertNotIn('name', self.amenity.__dict__)
        self.assertIn('name', Amenity.__dict__)
        self.assertEqual(Amenity.name, '')
        self.assertIs(type(Amenity.name), str)
