import unittest
from app import flask_app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        #Seting up the test client
        self.app = flask_app.test_client()
        self.app.testing = True

    def test_index_1(self):
        #Sending a GET request to the "/" route
        response = self.app.get("/")

        #Checking if the response is 200 OK
        self.assertEqual(first=response.status_code, second=200)