#!/usr/bin/python3
"""Test for state"""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class TestState(TestBasemodel):
    """Represents the tests for the State model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests the type of name."""
        brnad = self.value()
        self.assertEqual(
            type(brnad.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
