import unittest
import json
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app.app import create_app
from app.v2.migration import Database
db = Database()
cur = db.cur

class TestSetup(unittest.TestCase):
    """Base test class for all test classes"""

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.new_user = {
            "username": "test1",
            "email": "test@example.com",
            "password": "testpass"
        }
        self.new_user2 = {
            "username": "test",
            "email": "test@example.com",
            "password": "testpass"
        }
        self.new_user3 = {
            "username": "test1",
            "email": "test@example.",
            "password": "testpass"
        }
        self.new_user4 = {
            "username": "test1",
            "email": "test@example.com",
            "password": "test"
        }



    def tearDown(self):
        query = "DELETE FROM users WHERE username='test1';"
        cur.execute(query)
        db.conn.commit()
