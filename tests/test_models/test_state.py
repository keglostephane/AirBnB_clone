#!/usr/bin/python3
"""Unittest for State class
"""
import unittest
from models.state import State


class testState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Create State instance for tests"""
        self.state = State()

    def tearDown(self):
        """Destroy State instance after tests"""
        del self.state

    def testStateClassPublicAttributes(self):
        """Test if State class have public attributes"""
        self.assertNotIn('name', self.state.__dict__)
        self.assertIn('name', State.__dict__)
        self.assertEqual(State.name, '')
        self.assertIs(type(State.name), str)
