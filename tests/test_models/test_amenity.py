#!/usr/bin/python3
"""unittests for Amenity"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """class TestAmenity"""
    def test_amenity(self):
        """testing for a type of the attributes and
        if attributes are not empty"""
        amenity = Amenity()
        self.assertIsNotNone(amenity.id)
        self.assertIsNotNone(amenity.created_at)
        self.assertIsNotNone(amenity.updated_at)
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime.datetime)
        self.assertIsInstance(amenity.updated_at, datetime.datetime)
        self.assertIsNotNone(amenity.name)

if __name__ == '__main__':
    unittest.main()
