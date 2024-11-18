import unittest
from app import flask_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        #Setting up test client
        self.client = flask_app.test_client()  

    def test_home_route_invalid_method(self):
        """Test that sending a POST request to a GET route returns a 405 status code."""
        response = self.client.post('/') 
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()