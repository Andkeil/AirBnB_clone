#!/usr/bin/python3
"""unittests for City"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """class TestCity"""
    def test_city(self):
        """testing for a type of the attributes and
        if attributes are not empty"""
        city = City()
        self.assertIsNotNone(city.id)
        self.assertIsNotNone(city.created_at)
        self.assertIsNotNone(city.updated_at)
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime.datetime)
        self.assertIsInstance(city.updated_at, datetime.datetime)
        self.assertIsNotNone(city.name)
        self.assertIsNotNone(city.state_id)

if __name__ == '__main__':
    unittest.main()
