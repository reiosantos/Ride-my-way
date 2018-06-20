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

    def test_delete_ride(self):
        """
        Test case for ride delete ride endpoint, it deletes a rides given its id
        """

        res = self.client().delete('/api/v1/rides/delete/4e')
        self.assertEqual(res.status_code, 404)

        res = self.client().delete('/api/v1/rides/delete/8')
        self.assertEqual(res.status_code, 404)

        res = self.client().delete('/api/v1/rides/delete/2')
        self.assertEqual(res.status_code, 200)
        self.assertIn("data", res.json)
        self.assertNotIn("error_message", res.json)
        self.assertIn("success_message", res.json)
        self.assertTrue(res.json['data'])
        self.assertTrue(res.json['success_message'])
