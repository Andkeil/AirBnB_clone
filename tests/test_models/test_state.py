#!/usr/bin/python3
"""unittests for State"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """class TestState"""
    def test_state(self):
        """testing for a type of the attributes and
        if attributes are not empty"""
        state = State()
        self.assertIsNotNone(state.id)
        self.assertIsNotNone(state.created_at)
        self.assertIsNotNone(state.updated_at)
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime.datetime)
        self.assertIsInstance(state.updated_at, datetime.datetime)
        self.assertIsNotNone(state.name)

if __name__ == '__main__':
    unittest.main()
