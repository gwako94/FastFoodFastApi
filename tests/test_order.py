import unittest
import json
from app.app import create_app


class TestOrder(unittest.TestCase):
    """ This class represents the order test case"""

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.add_order = {
            "items": "Burger",
            "price": "600",
            "quantity": 1
        }

    def test_order_placement(self):
        """ Test new order can be added """
 
        #place an order
        res = self.client.post('api/v1/orders', data=json.dumps(self.add_order), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Order placed successfully", msg["message"])
        
    def test_get_all_orders(self):
        """ Test all orders can be retrived """
        
        # Place an order
        self.client.post('api/v1/orders', 
                            data=json.dumps(self.add_order), 
                            content_type='application/json')

        # get orders
        res = self.client.get('api/v1/orders', content_type='application/json')
        self.assertEqual(res.status_code, 200)


    def test_orders_not_found(self):
        """ Test when no orders exists """
        res = self.client.get('api/v1/orders', content_type='application/json')
        self.assertEqual(res.status_code, 404)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("No orders found!", msg["message"])
        
    def test_fetch_a_specific_order(self):
        """ Test a single order can be retrieved """
        # Place an order
        res = self.client.post('api/v1/orders', 
                                data=json.dumps(self.add_order),
                                content_type='application/json')
        
        res = self.client.get('api/v1/orders/1', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        
    def test_specific_order_not_found(self):
        """Test when a specific order is missing """
        res = self.client.get('api/v1/orders/27', content_type='application/json')
        self.assertEqual(res.status_code, 404)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Order not found!", msg["message"])
        
        
    def test_update_order_status(self):
        """Test that order status can be updated accordingly"""
        # Place an order
        self.client.post('api/v1/orders', data=json.dumps(self.add_order), content_type='application/json')
        res = self.app.put('api/v1/orders/1', data=json.dumps(dict(status = "completed")), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Order updated successfully", msg['message'])
         
if __name__ == '__main__':
    unittest.main()
    
    