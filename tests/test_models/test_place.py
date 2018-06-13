#!/usr/bin/python3
"""unittests for Place"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """class TestPlace"""
    def test_place(self):
        """testing for a type of the attributes and
        if attributes are not empty"""
        place = Place()
        self.assertIsNotNone(place.id)
        self.assertIsNotNone(place.created_at)
        self.assertIsNotNone(place.updated_at)
        self.assertIsInstance(place.id, str)
        self.assertIsInstance(place.created_at, datetime.datetime)
        self.assertIsInstance(place.updated_at, datetime.datetime)
        self.assertIsNotNone(place.city_id)
        self.assertIsNotNone(place.user_id)
        self.assertIsNotNone(place.name)
        self.assertIsNotNone(place.description)
        self.assertIsNotNone(place.number_rooms)
        self.assertIsNotNone(place.number_bathrooms)
        self.assertIsNotNone(place.max_guest)
        self.assertIsNotNone(place.price_by_night)
        self.assertIsNotNone(place.latitude)
        self.assertIsNotNone(place.longitude)
        self.assertIsNotNone(place.amenity_ids)
if __name__ == '__main__':
    unittest.main()
