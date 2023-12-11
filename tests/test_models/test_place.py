#!/usr/bin/python3
"""Unittest for Place class
"""
import unittest
from models.place import Place


class testPlace(unittest.TestCase):
    """Test the Place class"""

    def setUp(self):
        """Create an instance of Place for tests"""
        self.place = Place()

    def tearDown(self):
        """Destroy Place instance after tests"""
        del self.place

    def test_PlaceClassAttributes(self):
        """Test if Place class have public attributes"""
        self.assertNotIn('city_id', self.place.__dict__)
        self.assertNotIn('user_id', self.place.__dict__)
        self.assertNotIn('name', self.place.__dict__)
        self.assertNotIn('description', self.place.__dict__)
        self.assertNotIn('number_rooms', self.place.__dict__)
        self.assertNotIn('number_bathrooms', self.place.__dict__)
        self.assertNotIn('max_guest', self.place.__dict__)
        self.assertNotIn('price_by_night', self.place.__dict__)
        self.assertNotIn('latitude', self.place.__dict__)
        self.assertNotIn('longitude', self.place.__dict__)
        self.assertNotIn('amenity_ids', self.place.__dict__)

        self.assertIn('city_id', Place.__dict__)
        self.assertIn('user_id', Place.__dict__)
        self.assertIn('name', Place.__dict__)
        self.assertIn('description', Place.__dict__)
        self.assertIn('number_rooms', Place.__dict__)
        self.assertIn('number_bathrooms', Place.__dict__)
        self.assertIn('max_guest', Place.__dict__)
        self.assertIn('price_by_night', Place.__dict__)
        self.assertIn('latitude', Place.__dict__)
        self.assertIn('longitude', Place.__dict__)
        self.assertIn('amenity_ids', Place.__dict__)

        self.assertEqual(Place.city_id, '')
        self.assertEqual(Place.user_id, '')
        self.assertEqual(Place.name, '')
        self.assertEqual(Place.description, '')
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

        self.assertIs(type(Place.city_id), str)
        self.assertIs(type(Place.user_id), str)
        self.assertIs(type(Place.name), str)
        self.assertIs(type(Place.description), str)
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(type(Place.amenity_ids), list)
