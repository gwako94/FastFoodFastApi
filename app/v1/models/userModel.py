class User(object):
    """Implemetnts user class"""
    def __init__(self):
        self.users = {}

    def register_user(self, username, email, password, confirm_password):
        new_user = {
            "username": username,
            "email": email,
            "password": password,
            "confirm_password": confirm_password
        }
        user_id = str(len(self.users) + 1)
        self.users[user_id] = new_user
        return self.users