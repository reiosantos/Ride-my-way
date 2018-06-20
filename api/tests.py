"""
Tests module
"""
from unittest import TestCase

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
