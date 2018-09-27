import unittest
import json
import os
import sys
import inspect
import psycopg2

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app.app import create_app
from app.v2.migration import Database


db = Database()


class TestUser(unittest.TestCase):
    #set up test data
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.new_user = {
            "username": "test",
            "email": "test@example.com",
            "password": "testpass"
        }

    def test_register_new_user(self):
        """ Test new user register """

        # register a user
        res = self.client.post(
            '/auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        self.assertEqual(res.status_code, 201)
        self.assertTrue(res.content_type == 'application/json')