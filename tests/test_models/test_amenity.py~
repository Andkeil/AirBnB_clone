#!/usr/bin/python3
"""unittests for BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """class TestBAseModel"""
    def test_class(self):
        """testing for a type of the attributes and
        if attributes are not empty"""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()
