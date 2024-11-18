import unittest
from app import flask_app

#Test1
class TestRoutes(unittest.TestCase):
    def setUp(self):
        #Setting up test client
        self.client = flask_app.test_client()  

    def test_home_route(self):        
        # Testing the '/' route which is expected to only handle GET requests.

        # -> Expected Output: The server should return a 405 Method Not Allowed status code
          
        # -> Actual Result: If the actual result is 405, the test will pass, indicating 
        #   that the route is correctly handling the invalid request method.

        #Sending a post request to the route
        response = self.client.post('/') 
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()