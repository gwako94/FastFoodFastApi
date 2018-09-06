import datetime


now = datetime.datetime.now()


class Menu(object):

    """Implements the menu class"""

    def __init__(self):
        self.menu = {
            "burger": 500,
                "milkshake": 300,
                "friedchicken": 600
        }

    def get_item_price(self, item_name):
        return self.menu[item_name]


class Order(object):

    """ Implements order class"""

    def __init__(self):
        self.orders = {}

    def place_order(self, user, cart={"item": 0}, total=0):
        new_order = {
            "id": str(len(self.orders) + 1),
                "cart": cart,
                "status": "pending",
                "created_at": now
        }
        self.orders[user] = new_order
        return self.orders

    def get_all_orders(self):
        if self.orders:
            return self.orders

    def get_order_by_id(self, order_id):
        """ Fetch a specific order using given id"""
        if self.orders:
            for order in self.orders.values():
                if order["id"] == order_id:
                    return order

    def update_order(self, order_id, updated_at=now):
        """ Method to update status of an order"""
        updated_order = self.get_order_by_id(order_id)
        if updated_order:
            updated_order["status"] = "completed"
            updated_order["updated_at"] = updated_at
            return updated_order
