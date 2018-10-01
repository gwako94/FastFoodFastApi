import unittest
import json

#import local files
from tests.test_v2_base import TestSetup

class TestUser(TestSetup):
    
    def test_register_new_user(self):
        """ Test new user register """

        # register a user
        res = self.client.post(
            '/v2/auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('User Registered successfully!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')

    def test_register_already_registered_user(self):
        """ Test existing user register """

        # register a user
        self.client.post(
            '/v2/auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')
            
        #try registering the user again
        res = self.client.post(
            '/v2/auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('User already exists!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 400)

    def test_register_with_invalid_username(self):
        """Test invalid username"""
        res = self.client.post(
            '/v2/auth/register',
            data=json.dumps(self.new_user2),
            content_type='application/json')

        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('letters or numbers', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 400)
        
    def test_register_with_invalid_email(self):
        """Test invalid email"""
        res = self.client.post(
            '/v2/auth/register',
            data=json.dumps(self.new_user3),
            content_type='application/json')

        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('Please input a valid email!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 400)

    def test_register_with_invalid_password(self):
        res = self.client.post(
            '/v2/auth/register',
            data=json.dumps(self.new_user4),
            content_type='application/json')

        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn('must be atlist 6 characters', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 400)
    
    def test_registered_user_login(self):
        self.client.post(
            '/v2/auth/register',
            data=json.dumps(self.new_user),
            content_type='application/json')

        res = self.client.post(
            '/v2/auth/login',
            data=json.dumps(self.new_user),
            content_type='application/json')
        msg = json.loads(res.data.decode('UTF-8'))
        self.assertIn('Login success!', msg['message'])
        self.assertTrue(res.content_type == 'application/json')
        self.assertEqual(res.status_code, 200)
