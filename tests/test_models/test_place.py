#!/usr/bin/python3
"""test module for place """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """Represents the tests for the Place model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_cid(self):
        """Tests  city_id."""
        brand = self.value()
        self.assertEqual(
            type(brand.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_uid(self):
        """Tests  user_id."""
        brand = self.value()
        self.assertEqual(
            type(brand.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def testn(self):
        """Tests name."""
        brand = self.value()
        self.assertEqual(
            type(brand.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_des(self):
        """Tests description."""
        brand = self.value()
        self.assertEqual(
            type(brand.description),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_room(self):
        """Tests number rooms."""
        brand = self.value()
        self.assertEqual(
            type(brand.number_rooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_bathrooms(self):
        """Tests number bathrooms."""
        brand = self.value()
        self.assertEqual(
            type(brand.number_bathrooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_maxg(self):
        """Tests max_guest."""
        brand = self.value()
        self.assertEqual(
            type(brand.max_guest),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_pbn(self):
        """Tests price_by_night."""
        brand = self.value()
        self.assertEqual(
            type(brand.price_by_night),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_lat(self):
        """Tests latitude."""
        brand = self.value()
        self.assertEqual(
            type(brand.latitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_long(self):
        """Tests longitude."""
        brand = self.value()
        self.assertEqual(
            type(brand.longitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_aids(self):
        """Tests amenity_ids."""
        brand = self.value()
        self.assertEqual(type(new.amenity_ids), list)
