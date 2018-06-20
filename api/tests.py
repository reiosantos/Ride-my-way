"""
Tests module
"""
from unittest import TestCase

from flask import json

from api.app import APP


class TestClass(TestCase):
    """
    Tests run for the api
    """
    def setUp(self):
        self.app = APP
        self.client = self.app.test_client

    def test_post_ride(self):
        """
        Test case for get rides endpoint, it gets all rides
        """
        res = self.client().post('/api/v1/rides/', data=json.dumps(dict(passenger_name=False, ride_date="")),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 206)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], list)
        self.assertEqual(res.json['error_message'], "some of these fields are missing")

        res = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver=False, driver_contact="0789234567", trip_to="namayuba", cost=34000)),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 206)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json['error_message'], "some of these fields have empty/no values")

        res = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver="sseks", driver_contact="", trip_to="", cost=34000)),
                                 content_type='application/json')
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json['error_message'], "some of these fields have empty/no values")

        res = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver="sseks", driver_contact="078936d783u", trip_to="kasubi", cost=34000)),
                                 content_type='application/json')
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertIn("is wrong", res.json['error_message'])

        res = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver="kasa", driver_contact="0789234567", trip_to="namayuba", cost="34000")),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertNotIn("error_message", res.json)
        self.assertIn("success_message", res.json)
        self.assertTrue(res.json['data'])
        self.assertEqual(res.json['success_message'], "successfully added to entry to rides")
