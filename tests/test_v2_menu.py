import unittest
import json
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from tests.test_v2_base import TestSetup


class TestMenu(TestSetup):

    """Menu testcases"""

    def test_admin_can_post_menu(self):
        """Test admin can post menu"""
        res = self.client.post(
            'api/v2/menu',
            data=json.dumps(self.new_menu),
            content_type='application/json',
            headers={'access-token': self.admin_token})
        self.assertEqual(res.status_code, 201)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Menu created!", msg["message"])

    def test_non_admin_cannot_post_menu(self):
        """ Test non admin cannot post menu"""
        res = self.client.post(
            'api/v2/menu',
            data=json.dumps(self.new_menu),
            content_type='application/json',
            headers={'access-token': self.token})
        self.assertEqual(res.status_code, 403)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Cannot perform this function!", msg["message"])

    def test_existing_menu(self):
        """Test existing menu"""
        # post a menu
        self.client.post(
            'api/v2/menu',
            data=json.dumps(self.new_menu),
            content_type='application/json',
            headers={'access-token': self.admin_token})
        res = self.client.post(
            'api/v2/menu',
            data=json.dumps(self.new_menu),
            content_type='application/json',
            headers={'access-token': self.admin_token})
        self.assertEqual(res.status_code, 409)
        msg = json.loads(res.data.decode("UTF-8"))
        self.assertIn("Menu already exists!", msg["message"])
