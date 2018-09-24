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
from app.v1.models.userModel import User
from app.v1.models.orderModel import Order
user = User()
order = Order()

class TestOrder(unittest.TestCase):

    """ This class represents the order test case"""

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

    def test_order_placement(self):
        """ Test new order can be added """

        # place an order
        res = self.client.post(
            'api/v1/orders',
            data=json.dumps(self.add_order),
            content_type='application/json',
            headers=
            {'x-access-token': self.token})
        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Order placed successfully", msg["message"])

    def test_get_all_orders(self):
        """ Test all orders can be retrived """

        # Place an order
        self.client.post('api/v1/orders',
                         data=json.dumps(self.add_order),
                         content_type='application/json',
                         headers=
                            {'x-access-token': self.token})

        # get orders
        res = self.client.get('api/v1/orders', 
                               content_type='application/json',
                               headers=
                                {'x-access-token': self.token})
        self.assertEqual(res.status_code, 200)

    def test_fetch_a_specific_order(self):
        """ Test a single order can be retrieved """
        # Place an order
        res = self.client.post('api/v1/orders',
                               data=json.dumps(self.add_order),
                               content_type='application/json',
                               headers=
                                {'x-access-token': self.token})

        res = self.client.get(
            'api/v1/orders/1',
            content_type='application/json',
            headers=
            {'x-access-token': self.token})
        self.assertEqual(res.status_code, 200)

    def test_specific_order_not_found(self):
        """Test when a specific order is missing """
        res = self.client.get(
            'api/v1/orders/27',
            content_type='application/json',
            headers=
            {'x-access-token': self.token})
        self.assertEqual(res.status_code, 404)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Order not found!", msg["message"])

    def test_update_order_status(self):
        """Test that order status can be updated accordingly"""
        # Place an order
        self.client.post(
            'api/v1/orders',
            data=json.dumps(self.add_order),
            content_type='application/json',
            headers=
            {'x-access-token': self.token})
        res = self.client.put(
            'api/v1/orders/1',
            data=json.dumps(dict(status="completed")),
            content_type='application/json',
            headers=
            {'x-access-token': self.token})
        self.assertEqual(res.status_code, 200)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Order updated successfully", msg['message'])
        
    def tearDown(self):
        self.users = user.users
        self.orders = order.orders
        self.users.clear()
        self.orders.clear()

if __name__ == '__main__':
    unittest.main()
