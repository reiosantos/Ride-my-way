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

        res = self.client().put('/api/v1/rides/update/', data=json.dumps(
            dict(trip_to="kabumbi", cost="4000")), content_type='application/json')
        self.assertEqual(res.status_code, 206)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], list)
        self.assertEqual(res.json['error_message'], "some of these fields are missing")

        res = self.client().put('/api/v1/rides/update/', data=json.dumps(
            dict(trip_to="kitunda", cost="4000", ride_id=8, status="available", taken_by=None)),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 404)
        self.assertIn("data", res.json)
        self.assertFalse(res.json['data'])
        self.assertIn("error_message", res.json)

        res = self.client().put('/api/v1/rides/update/', data=json.dumps(
            dict(trip_to="kitunda", cost="4000", ride_id=None, status="available", taken_by=None)),
                                content_type='application/json')
        self.assertEqual(res.status_code, 206)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json['error_message'], "Ride id is missing a value")

        res = self.client().put('/api/v1/rides/update/', data=json.dumps(
            dict(trip_to="kitunda", cost="4000", ride_id=2, status="available", taken_by=None)),
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertNotIn("error_message", res.json)
        self.assertIn("success_message", res.json)
        self.assertTrue(res.json['data'])
        self.assertTrue(res.json['success_message'])
