import unittest
import json
from werkzeug.security import generate_password_hash, check_password_hash
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app.app import create_app
from app.v2.migration import Database
from app.v2.models.userModel import User
db = Database()
cur = db.cur

class TestSetup(unittest.TestCase):
    """Base test class for all test classes"""

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.new_user = {
            "username": "test1",
            "email": "test@example.com",
            "password": "testpass"
        }
        self.new_user2 = {
            "username": "test",
            "email": "test@example.com",
            "password": "testpass"
        }
        self.new_user3 = {
            "username": "test1",
            "email": "test@example.",
            "password": "testpass"
        }
        self.new_user4 = {
            "username": "test1",
            "email": "test@example.com",
            "password": "test"
        }
        self.new_menu = {
            "item_name": "test_burger",
	        "image_url": "burger.jpg",
	        "price": "300"
        }
        self.admin1 = {
            "username": "Admin2",
            "email": "admin2@example.com",
            "password": "@admin2"
        }
        hashed_password = generate_password_hash('@admin2', method='sha256')
        admin_details = User(
            'Admin2',
            'admin2@example.com',
            hashed_password,
            True
        )
        admin_details.register_user()
        self.Nadmin = {
            "username": "user1",
            "email": "user1@example.com",
            "password": "@user1"
        }
        hashed_password = generate_password_hash('@user1', method='sha256')
        user_details = User(
            'user1',
            'user1@example.com',
            hashed_password,
        )
        user_details.register_user()
        
        self.admin_login = self.client.post(
            '/v2/auth/login',
            data=json.dumps(self.admin1),
            content_type='application/json')
        self.data = json.loads(self.admin_login.data.decode("UTF-8"))
        self.admin_token = self.data['token']
        
        self.login = self.client.post(
            '/v2/auth/login',
            data=json.dumps(self.Nadmin),
            content_type='application/json')
        self.data = json.loads(self.login.data.decode("UTF-8"))
        self.token = self.data['token']


    def tearDown(self):
        user = "DELETE FROM users WHERE username='test1';"
        menu = "DELETE FROM menu WHERE item_name='test_burger';"
        queries = [user, menu]
        for query in queries:
            cur.execute(query)
            db.conn.commit()
