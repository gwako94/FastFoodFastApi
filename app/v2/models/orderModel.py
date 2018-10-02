import datetime
import json


#import local files
from ..migration import Database
from app.v2.models.menuModel import Menu

now = datetime.datetime.now()
db = Database()
cur = db.cur


class Order(object):

    """Implements order class"""

    # order constructor

    def __init__(self, user_id=0, cart={"item": 0}, total=0, status="new", created_at=now):
        self.user_id = user_id
        self.cart = cart
        self.total = total
        self.status = status
        self.created_at = created_at

    def add_order(self):
        query = "INSERT INTO orders (user_id, cart, total, status, created_at) values (%s, %s, %s, %s, %s);"
        cur.execute(
            query,
            (self.user_id,
             json.dumps(
                 self.cart),
             self.total,
             self.status,
             self.created_at))
        db.conn.commit()
        return True

    @staticmethod
    def get_all_orders():
        query = "SELECT * from orders;"
        cur.execute(query)
        all_orders = cur.fetchall()
        if all_orders:
            orders = [{
                "id": order["order_id"],
                "user_id": order["user_id"],
                "cart": json.loads(order["cart"]),
                "total": str(order["total"]),
                "status": order["status"],
                "created_at": order["created_at"]
            } for order in all_orders]
            return orders
        return False

        
    @staticmethod
    def get_order_by_id(order_id):
        query = "SELECT * FROM orders WHERE order_id=%s;"
        cur.execute(query, (order_id, ))
        order = cur.fetchone()
        if order:
            the_order = {
                "id": order["order_id"],
                "user_id": order["user_id"],
                "cart": json.loads(order["cart"]),
                "total": str(order["total"]),
                "status": order["status"],
                "created_at": order["created_at"]
            }
            return the_order
        return False
    @staticmethod
    def update_order(order_id, status, updated_at):
        """ Method to update status of an order"""
        updated_order = Order.get_order_by_id(order_id)
        if updated_order:
            updated_order["status"] = status
            updated_order["updated_at"] = updated_at
            return updated_order


    @staticmethod
    def get_total(cart):
        """Methods gets total cost of cart items"""
        total = 0
        for item, quantity in cart.items():
            price = Menu.get_item_price(item)
            try:
                total += price['price'] * quantity
                    
            except TypeError:
                return False
        return total
