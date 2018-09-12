import uuid



class User(object):

    """Implemetnts user class"""

    def __init__(self):
        self.users = {}

    def register_user(self, username, email, password):
        new_user = {
            "public_id": str(uuid.uuid4()),
            "username": username,
            "email": email,
            "password": password,
            "admin": False
        }
        self.users[username] = new_user
        return self.users

    def get_users(self):
        if self.users:
            return self.users
