import datetime
from ..migration import Database

now = datetime.datetime.now()
db = Database()
cur = db.conn.cursor()
class Menu(object):
    """Implements menu class"""

    # Menu constructor
    def __init__(self, item_name, image_url, price):
        self.item_name = item_name
        self.image_url = image_url
        self.price = price
        self.created_at = now

        self.cur = db.conn.cursor()

    def add_menu(self):
        query = "INSERT INTO menu (item_name, image_url, price, created_at) values (%s, %s, %s, %s);"
        cur.execute(query, (self.item_name, self.image_url, self.price, self.created_at))
        db.conn.commit()
        cur.close()