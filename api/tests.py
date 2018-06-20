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

    def test_request_for_ride(self):
        """
        Test case for ride requests endpoint, it updates rides
        """

        res = self.client().post('/api/v1/rides/requests/join/', data=json.dumps(
            dict(passenger_contact=False, passenger="")), content_type='application/json')
        self.assertEqual(res.status_code, 206)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], list)
        self.assertEqual(res.json['error_message'], "some of these fields are missing")

        res = self.client().post('/api/v1/rides/requests/join/', data=json.dumps(
            dict(passenger="kitunda", passenger_contact="0789234567", ride_id=8)),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 404)
        self.assertIn("data", res.json)
        self.assertFalse(res.json['data'])
        self.assertIn("error_message", res.json)

        res = self.client().post('/api/v1/rides/requests/join/', data=json.dumps(
            dict(passenger="sseks", passenger_contact="", ride_id=2)),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 206)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json['error_message'], "some of these fields have empty/no values")

        res = self.client().post('/api/v1/rides/requests/join/', data=json.dumps(
            dict(passenger="sseks", passenger_contact="9871234768", ride_id=2)),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertNotIn("error_message", res.json)
        self.assertIn("success_message", res.json)
        self.assertTrue(res.json['data'])
        self.assertTrue(res.json['success_message'])
