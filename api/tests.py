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

    def test_get_rides(self):
        """
        Test case for get rides endpoint, it gets all rides
        """
        res = self.client().get('/api/v1/rides/')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertIsInstance(res.json['data'], list)
        self.assertTrue(res.json["data"])
        self.assertIsInstance(res.json["data"][0], dict)

    def test_get_one_ride(self):
        """
        Test case for get rides endpoint, it gets all rides
        """
        res = self.client().get('/api/v1/rides/er')

        self.assertEqual(res.status_code, 404)

        res = self.client().get('/api/v1/rides/@')
        self.assertEqual(res.status_code, 404)

        res = self.client().get('/api/v1/rides/5')
        self.assertEqual(res.status_code, 404)

        res = self.client().get('/api/v1/rides/3')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json["data"]['ride_id'], 3)

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
