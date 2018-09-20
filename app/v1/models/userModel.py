class User(object):

    """Implemetnts user class"""

    def __init__(self):
        self.users = {}

    def register_user(self, username, email, password):
        new_user = {
            "id": str(len(self.users) + 1),
            "username": username,
            "email": email,
            "password": password,
            "admin": False
        }
        user_id = str(len(self.users) + 1)
        self.users[user_id] = new_user
        return self.users

    def get_users(self):
        if self.users:
            return self.users

    def get_user_by_id(self, user_id):
        if self.users:
            for user in self.users.values():
                if user['id'] == user_id:
                    return user
    def promote_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            user['admin'] = True
            return user