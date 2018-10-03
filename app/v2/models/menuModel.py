import datetime
from ..migration import Database

now = datetime.datetime.now()
db = Database()
cur = db.cur


class Menu(object):

    """Implements menu class"""

    # Menu constructor

    def __init__(self, item_name, image_url, price):
        self.item_name = item_name
        self.image_url = image_url
        self.price = price
        self.created_at = now

    def check_if_menu_exists(self, item_name):
        query = "SELECT item_name from menu WHERE item_name=%s;"
        cur.execute(query, (item_name,))
        menu = cur.fetchone()
        if menu:
            return True

    def add_menu(self):
        if self.check_if_menu_exists(self.item_name):
            return False
        query = "INSERT INTO menu (item_name, image_url, price, created_at) values (%s, %s, %s, %s);"
        cur.execute(
            query,
            (self.item_name,
             self.image_url,
             self.price,
             self.created_at))
        db.conn.commit()
        return True

    @staticmethod
    def get_all_menu():
        query = "SELECT * from menu;"
        cur.execute(query)
        menu = cur.fetchall()
        return menu

    @staticmethod
    def get_item_price(item_name):
        query = "SELECT price from menu where item_name=%s;"
        cur.execute(query, (item_name,))
        price = cur.fetchone()
        return price
