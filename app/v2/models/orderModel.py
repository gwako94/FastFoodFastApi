import datetime
from ..migration import Database

now = datetime.datetime.now()
db = Database()
cur = db.cur


class Order(object):

    """Implements order class"""

    # order constructor

    def __init__(self, user_id=1, cart={"item": 0}, total=0, status="new"):
        self.user_id = user_id
        self.cart = cart
        self.total = total
        self.status = status
