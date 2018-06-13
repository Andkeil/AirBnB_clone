#!/usr/bin/python3
"""unittests for review"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """class TestReview"""
    def test_review(self):
        """testing for a type of the attributes and
        if attributes are not empty"""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertIsNotNone(review.created_at)
        self.assertIsNotNone(review.updated_at)
        self.assertIsInstance(review.id, str)
        self.assertIsInstance(review.created_at, datetime.datetime)
        self.assertIsInstance(review.updated_at, datetime.datetime)
        self.assertIsNotNone(review.place_id)
        self.assertIsNotNone(review.user_id)
        self.assertIsNotNone(review.text)

if __name__ == '__main__':
    unittest.main()
