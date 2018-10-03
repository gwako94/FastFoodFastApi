import datetime
from ..migration import Database

now = datetime.datetime.now()
db = Database()
cur = db.conn.cursor()


class User(object):

    """ Implements user class"""

    def __init__(self, username, email, password, admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin
        self.created_at = now

    def check_if_user_exists(self, username):
        query = "SELECT username from users WHERE username=%s;"
        cur.execute(query, (username,))
        the_user = cur.fetchone()
        if the_user:
            return True

    def register_user(self):
        if self.check_if_user_exists(self.username):
            return False
        query = "INSERT INTO users (username, email, password, admin, created_at) VALUES (%s, %s, %s, %s, %s);"
        cur.execute(
            query,
            (self.username,
             self.email,
             self.password,
             self.admin,
             self.created_at))
        db.conn.commit()
        return True

    @staticmethod
    def get_user_by_id(user_id):
        query = "SELECT * FROM users WHERE id=%s;"
        cur.execute(query, (user_id, ))
        user = cur.fetchone()
        if user:
            return user
        return False