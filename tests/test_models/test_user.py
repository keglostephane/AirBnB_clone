#!/usr/bin/python3
"""Unittest for User class
"""
import unittest
import json
from models.user import User
from models import storage


class testUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Create User instance for tests"""
        self.user = User()

    def tearDown(self):
        """Destroy User instance after tests"""

    def testUserClassPublicAttributes(self):
        """Test if User class have public attributes"""
        self.assertNotIn('email', self.user.__dict__)
        self.assertNotIn('password', self.user.__dict__)
        self.assertNotIn('last_name', self.user.__dict__)
        self.assertNotIn('first_name', self.user.__dict__)
