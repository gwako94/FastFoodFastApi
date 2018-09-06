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


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.new_user = {
            "username": "gwako",
            "email": "g@example.com",
            "password": "qwerty12",
        }

    def test_register_user(self):
        """ Test new user can be created! """

        # register a user
        res = self.client.post(
            '/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("User Registered successfully!", msg["message"])

if __name__ == '__main__':
    unittest.main()
