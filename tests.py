import unittest
from unittest import mock
import json
import subprocess
from flask import Flask
from flask.testing import FlaskClient

from app import app

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.payload = {
            "technologies": [
                "rust",
                "terraform",
                "ansible"
            ],
            "user_id" : '64ade9f240ea4eaa1c1498b2'
        }

    @mock.patch('subprocess.call')
    def test_api_call(self, mock_subproc_call):
        response = self.app.post('/', json=self.payload)

        # Verify the response status code
        self.assertEqual(response.status_code, 200)

        # Verify the response message
        self.assertEqual(response.get_data(as_text=True), 'install finished')

        # Verify subprocess execution
        mock_subproc_call.assert_called_once()
        # self.assertEqual(subprocess.run.call_args[0][0], ['ansible-playbook', '-i', 'inventory.ini', 'playbook.yml'])
        # self.assertEqual(subprocess.run.call_args[1]['cwd'], '/ansible')

if __name__ == '__main__':
    unittest.main()
