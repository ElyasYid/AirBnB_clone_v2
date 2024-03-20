#!/usr/bin/python3
"""Test fir user  """
import os
from sqlalchemy import Column

from tests.test_models.test_base_model import TestBasemodel
from models.user import User


class TestUser(TestBasemodel):
    """Represents the tests for the User model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_fime(self):
        """Tests the type of first_name."""
        bowser = self.value()
        self.assertEqual(
            type(bowser.first_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_lne(self):
        """Tests the type of last_name."""
        bowser = self.value()
        self.assertEqual(
            type(bowser.last_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_eil(self):
        """Tests the type of email."""
        bowser = self.value()
        self.assertEqual(
            type(bowser.email),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_pad(self):
        """Tests the type of password."""
        bowser = self.value()
        self.assertEqual(
            type(bowser.password),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
