#!/usr/bin/python3
"""Unittest for User class
"""
import unittest
from models.user import User


class testUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Create User instance for tests"""
        self.user = User()

    def tearDown(self):
        """Destroy User instance after tests"""
        del self.user

    def testUserClassPublicAttributes(self):
        """Test if User class have public attributes"""
        self.assertNotIn('email', self.user.__dict__)
        self.assertNotIn('password', self.user.__dict__)
        self.assertNotIn('last_name', self.user.__dict__)
        self.assertNotIn('first_name', self.user.__dict__)

        self.assertIn('email', User.__dict__)
        self.assertIn('password', User.__dict__)
        self.assertIn('last_name', User.__dict__)
        self.assertIn('first_name', User.__dict__)

        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')
        self.assertEqual(User.last_name, '')
        self.assertEqual(User.first_name, '')

        self.assertIs(type(User.email), str)
        self.assertIs(type(User.password), str)
        self.assertIs(type(User.last_name), str)
        self.assertIs(type(User.first_name), str)
