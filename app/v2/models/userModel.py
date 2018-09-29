import datetime
from ..migration import Database

now = datetime.datetime.now()
db = Database()
cur = db.conn.cursor()
class User(object):

    """ Implements user class"""
    def __init__(self, username, email, password, admin=True):
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin
        self.created_at = now
        
    def register_user(self):
        query = "INSERT INTO users (username, email, password, admin, created_at) VALUES (%s, %s, %s, %s, %s);"
        cur.execute(query, (self.username, self.email, self.password, self.admin, self.created_at))
        db.conn.commit()
        cur.close()