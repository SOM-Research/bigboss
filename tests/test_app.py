import unittest
import json
import sys
import os

# Add the project directory to the system path to import the routes module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_testing import TestCase
from routes import app

class TestEthicAnalApp(TestCase):
    
    def create_app(self):
        """
        Create a Flask app for testing purposes.
        """
        app.config['TESTING'] = True
        return app

    def setUp(self):
        """
        Set up test variables before each test.
        """
        self.test_comment = {
            "comment_id": "123",
            "user": "test_user",
            "user_id": "1",
            "comment_body": "This is a test comment",
            "created_at": "2023-01-01",
            "updated_at": "2023-01-01",
            "repository_name": "test_repo",
            "repository_full_name": "test_org/test_repo",
            "repository_html_url": "http://github.com/test_org/test_repo",
            "issue_number": "1",
            "issue_title": "Test Issue",
            "issue_body": "This is a test issue",
            "issue_url": "http://github.com/test_org/test_repo/issues/1",
            "comment_url": "http://github.com/test_org/test_repo/issues/1#comment-1"
        }

    def test_analyze_comment(self):
        """
        Test the /analyze endpoint to ensure it processes comments correctly.
        """
        response = self.client.post('/analyze', data=json.dumps(self.test_comment), content_type='application/json')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('analysis', data)
        self.assertIn('classification', data['analysis'])
        self.assertIn('reasons', data['analysis'])
        self.assertIn('flags', data['analysis'])
        self.assertIn('numbered_flags', data['analysis'])

if __name__ == '__main__':
    unittest.main()
