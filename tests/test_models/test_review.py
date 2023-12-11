#!/usr/bin/python3
"""Unittest for Review class
"""
import unittest
from models.review import Review


class testReview(unittest.TestCase):
    """Tests the Review class"""

    def setUp(self):
        """Create Review instance for tests"""
        self.review = Review()

    def tearDown(self):
        """Destroy Review instance after tests"""
        del self.review

    def testReviewClassPublicAttribute(self):
        """Test if Review class have public attributes"""
        self.assertNotIn('place_id', self.review.__dict__)
        self.assertNotIn('user_id', self.review.__dict__)
        self.assertNotIn('text', self.review.__dict__)

        self.assertIn('place_id', Review.__dict__)
        self.assertIn('user_id', Review.__dict__)
        self.assertIn('text', Review.__dict__)

        self.assertEqual(Review.place_id, '')
        self.assertEqual(Review.user_id, '')
        self.assertEqual(Review.text, '')

        self.assertIs(type(Review.place_id), str)
        self.assertIs(type(Review.user_id), str)
        self.assertIs(type(Review.text), str)
