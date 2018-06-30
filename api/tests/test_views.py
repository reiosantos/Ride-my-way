"""
Tests module
"""
import os
import sys
import unittest
from unittest import TestCase

from flask import json

sys.path.append(os.path.pardir)
from api.run import APP


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
        self.assertIn("error_message", res.json)
        self.assertFalse(res.json['error_message'])
        self.assertIn("data", res.json)
        self.assertIsInstance(res.json['data'], list)
        self.assertTrue(res.json["data"])
        self.assertIsInstance(res.json["data"][0], dict)

    def test_get_one_ride(self):
        """
        Test case for get rides endpoint, it gets all rides
        """
        res = self.client().get('/api/v1/rides/0')
        self.assertEqual(res.status_code, 200)

        res = self.client().get('/api/v1/rides/er')
        self.assertEqual(res.status_code, 404)

        res = self.client().get('/api/v1/rides/@')
        self.assertEqual(res.status_code, 404)

        res = self.client().get('/api/v1/rides/5')
        self.assertEqual(res.status_code, 404)

        res = self.client().get('/api/v1/rides/2/')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json["data"]['ride_id'], 2)

    def test_post_ride(self):
        """
        Test case for get rides endpoint, it gets all rides
        """

        res = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver=False, driver_contact="0789234567", trip_to="namayuba", cost=34000)))
        self.assertEqual(res.status_code, 400)

        res = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver=False, driver_contact="0789234567", cost=34000)),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], list)
        self.assertEqual(res.json['error_message'], "some of these fields are missing")

        res = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver=False, driver_contact="0789234567", trip_to="namayuba", cost=34000)),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json['error_message'], "some of these fields have empty/no values")

        res = self.client().post('/api/v1/rides/', data=json.dumps(
            dict(driver="sseks", driver_contact="", trip_to="", cost=34000)),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 400)
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
        self.assertEqual(res.status_code, 201)
        self.assertIn("data", res.json)
        self.assertNotIn("error_message", res.json)
        self.assertIn("success_message", res.json)
        self.assertTrue(res.json['data'])
        self.assertEqual(res.json['success_message'], "successfully added a new ride.")

    def test_request_for_ride(self):
        """
        Test case for ride requests endpoint, it updates rides
        """

        res = self.client().post('/api/v1/rides/2/requests/', data=json.dumps(
            dict(passenger_contact=False)), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], list)
        self.assertEqual(res.json['error_message'], "some of these fields are missing")

        res = self.client().post('/api/v1/rides/8/requests/', data=json.dumps(
            dict(passenger="kitunda", passenger_contact="0789234567")),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 404)
        self.assertIn("data", res.json)
        self.assertFalse(res.json['data'])
        self.assertIn("error_message", res.json)

        res = self.client().post('/api/v1/rides/2/requests/', data=json.dumps(
            dict(passenger="sseks", passenger_contact="")),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json['error_message'], "some of these fields have empty/no values")

        res = self.client().post('/api/v1/rides/2/requests/', data=json.dumps(
            dict(passenger="sseks", passenger_contact="9871234768")),
                                 content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn("data", res.json)
        self.assertNotIn("error_message", res.json)
        self.assertIn("success_message", res.json)
        self.assertTrue(res.json['data'])
        self.assertTrue(res.json['success_message'])

    def test_update_ride(self):
        """
        Test case for ride requests endpoint, it tests updates to a rides
        """
        res = self.client().put('/api/v1/rides/update/', data=json.dumps(
            dict(trip_to="kabumbi", cost="4000")))
        self.assertEqual(res.status_code, 400)

        res = self.client().put('/api/v1/rides/update/', data=json.dumps(
            dict(trip_to="kabumbi", cost="4000")), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], list)
        self.assertEqual(res.json['error_message'], "some of these fields are missing")

        res = self.client().put('/api/v1/rides/update/', data=json.dumps(
            dict(trip_to="kitunda", cost="4000", status="available", taken_by=None)),
                                content_type='application/json')
        self.assertEqual(res.status_code, 400)

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
        self.assertEqual(res.status_code, 400)
        self.assertIn("data", res.json)
        self.assertIn("error_message", res.json)
        self.assertIsInstance(res.json['data'], dict)
        self.assertEqual(res.json['error_message'], "some of these fields have empty/no values")

        res = self.client().put('/api/v1/rides/update/', data=json.dumps(
            dict(trip_to="kitunda", cost="4000", ride_id=2, status="available", taken_by=None)),
                                content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertNotIn("error_message", res.json)
        self.assertIn("success_message", res.json)
        self.assertTrue(res.json['data'])
        self.assertTrue(res.json['success_message'])

    def test_delete_ride(self):
        """
        Test case for ride delete ride endpoint, it deletes a rides given its id
        """

        res = self.client().delete('/api/v1/rides/delete/4e')
        self.assertEqual(res.status_code, 404)

        res = self.client().delete('/api/v1/rides/delete/8')
        self.assertEqual(res.status_code, 404)

        res = self.client().delete('/api/v1/rides/delete/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertNotIn("error_message", res.json)
        self.assertIn("success_message", res.json)
        self.assertTrue(res.json['data'])
        self.assertTrue(res.json['success_message'])


if __name__ == "__main__":
    unittest.main()
