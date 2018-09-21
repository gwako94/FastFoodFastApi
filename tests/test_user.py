import unittest
import json
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app.app import create_app


class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()

        self.new_user = {
            "username": "test2",
            "email": "test2@example.com",
            "password": "test2pass"
        }
    def test_register_new_user(self):
        """ Test existing user register """

        # register a user
        res = self.client.post(
            '/auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('User Registered successfully!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')

    # def test_register_already_registered_user(self):
    #     """ Test existing user register """

    #     # register a user
    #     self.client.post(
    #         '/auth/register',
    #         data=json.dumps(self.new_user),
    #         content_type='application/json')
            
    #     #try registering the user again
    #     res = self.client.post(
    #         '/auth/register',
    #         data=json.dumps(self.new_user),
    #         content_type='application/json')

    #     msg = json.loads(res.data.decode("UTF-8"))
    #     self.assertIn('User already exists. Please Log in.', msg['message'])
    #     self.assertTrue(res.content_type == 'application/json')
    #     self.assertEqual(res.status_code, 400)

    def test_register_with_missing_username(self):
        self.new_user['username'] = ""
        res = self.client.post(
            'auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('Username cannot be empty!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 400)
        
    def test_register_with_missing_email(self):
        self.new_user['email'] = ""
        res = self.client.post(
            'auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('Email cannot be empty!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 400)

    def test_register_with_missing_password(self):
        self.new_user['password'] = ""
        res = self.client.post(
            'auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('Password cannot be empty!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 400)

    # def test_registered_user_login(self):
    #     self.client.post(
    #         'auth/register',
    #         data=json.dumps(self.new_user),
    #         content_type='application/json')

    #     res = self.client.post(
    #         'auth/login',
    #         data=json.dumps(self.new_user),
    #         content_type='application/json')

    #     self.assertTrue(res.content_type == 'application/json')
    #     self.assertEqual(res.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()
