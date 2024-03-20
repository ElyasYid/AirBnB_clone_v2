#!/usr/bin/python3
"""test module for class review"""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class TestReview(TestBasemodel):
    """Represents the tests for the Review model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_plid(self):
        """Tests the type of place_id."""
        toy = self.value()
        self.assertEqual(
            type(toy.place_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_uid(self):
        """Tests the type of user_id."""
        toy = self.value()
        self.assertEqual(
            type(toy.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_txt(self):
        """Tests the type of text."""
        toy = self.value()
        self.assertEqual(
            type(toy.text),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
