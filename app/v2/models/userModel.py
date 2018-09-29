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

    def check_if_user_exists(self, username, email):
        query = "SELECT username from users WHERE username=%s;"
        cur.execute(query, (username,))
        the_user = cur.fetchone()
        if the_user:
            return True
            
        query = "SELECT email from users WHERE email=%s;"
        cur.execute(query, (email,))
        the_user = cur.fetchone()
        if the_user:
            return True
        
        
    def register_user(self):
        if self.check_if_user_exists(self.username, self.email):
            return False
        query = "INSERT INTO users (username, email, password, admin, created_at) VALUES (%s, %s, %s, %s, %s);"
        cur.execute(query, (self.username, self.email, self.password, self.admin, self.created_at))
        db.conn.commit()