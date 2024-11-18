import unittest

from pymongo import MongoClient
from dotenv import load_dotenv
import os
from app import flask_app

class TestMongoDB(unittest.TestCase):
    def setUp(self):
        load_dotenv()

        self.app = flask_app.test_client()
        self.app.testing = True
        db_username = os.environ["MONGODB_USERNAME"]
        db_password = os.environ["MONGODB_PASSWORD"]
        self.client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.znx2q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  
    def test_mongodb_connection(self):
        """Test MongoDB connection using ping."""
        result = self.client.admin.command('ping')
        self.assertEqual(result['ok'], 1.0)

if __name__ == '__main__':
    unittest.main()



