import unittest
import json
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#import local files
from app.app import create_app
from app.v1.models.userModel import User
from app.v1.models.orderModel import Order

user = User()
order = Order()

class TestSetup(unittest.TestCase):
    """Base test class for all test classes"""


    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.add_order = {
            "user": "Galgallo",
                "cart": {"burger": 2}
        }
        self.new_user = {
            "username": "test2",
            "email": "test2@example.com",
            "password": "test2pass"
        }
        self.new_user2 = {
            "username": "test",
            "email": "test@example.com",
            "password": "testpass"
        }
        self.register = self.client.post(
            '/auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        self.login = self.client.post(
            '/auth/login',
            data=json.dumps(self.new_user),
            content_type='application/json')
        self.data = json.loads(self.login.data.decode("UTF-8"))
        self.token = self.data['token']

    def tearDown(self):
        self.users = user.users
        self.orders = order.orders
        self.users.clear()
        self.orders.clear()