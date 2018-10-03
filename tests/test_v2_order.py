import unittest
import json
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from tests.test_v2_base import TestSetup


class TestOrder(TestSetup):

    def test_order_placement(self):
        """ Test new order can be added """

        # place an order
        res = self.client.post(
            'api/v2/users/orders',
            data=json.dumps(self.order),
            content_type='application/json',
            headers={'access-token': self.token})
        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Order successfully placed!", msg["message"])

    def test_user_can_fetch_order_history(self):
        """Test user can fetch order history"""
        # post an order
        self.client.post(
            'api/v2/users/orders',
            data=json.dumps(self.order),
            content_type='application/json',
            headers={'access-token': self.token})

        # fetch order history
        res = self.client.get(
            'api/v2/users/orders',
                content_type='application/json',
                headers={'access-token': self.token})
        self.assertEqual(res.status_code, 200)

    def test_admin_can_get_all_orders(self):
        """Test admin can fetch all orders"""
        # post an order
        self.client.post(
            'api/v2/users/orders',
            data=json.dumps(self.order),
            content_type='application/json',
            headers={'access-token': self.token})
        res = self.client.get(
            'api/v2/orders',
                content_type='application/json',
                headers={'access-token': self.admin_token})
        self.assertEqual(res.status_code, 200)

    def test_order_not_found(self):
        res = self.client.get(
            'api/v2/orders/1000',
                content_type='application/json',
                headers={'access-token': self.admin_token})
        self.assertEqual(res.status_code, 404)
