import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from app import flask_app

class TestMongoDB(unittest.TestCase):
    def setUp(self):
        #Loading environment variables from .env file
        load_dotenv()

        self.app = flask_app.test_client()
        self.app.testing = True
        db_username = os.environ["MONGODB_USERNAME"]
        db_password = os.environ["MONGODB_PASSWORD"]
        self.client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.znx2q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client['test_db']  
        self.collection = self.db['test_collection']  

    #Test 2 - Database read operation
    """
        Test to verify the MongoDB connection by sending a ping command
        to the database and check response
    """
    def test_mongodb_connection(self):
        #Testing MongoDB connection using ping.
        result = self.client.admin.command('ping')
        self.assertEqual(result['ok'], 1.0)


    #Test 3 - Database write operation
    """
        Test to insert a document into the 'products' collection in MongoDB and verify that
        the insertion was successful
    """
    def test_write_data_to_db(self):
        #Defining new data to insert
        new_data = {
            "name": "test",
            "tag": "test tag",
            "price": 99.99
        }

        #Inserting the new data into the collection
        insert_result = self.collection.insert_one(new_data)

        #Ensuring the insert was successful by checking the inserted document
        inserted_data = self.collection.find_one({"name": "test"})
        
        self.assertIsNotNone(inserted_data, "Inserted data not found in the database.")
        self.assertEqual(inserted_data['name'], "test", "The name of the inserted data does not match the expected value.")
        self.assertEqual(inserted_data['tag'], "test tag", "The tag of the inserted data does not match the expected value.")
        self.assertEqual(inserted_data['price'], 99.99, "The price of the inserted data does not match the expected value.")

    def tearDown(self):
        #Cleaning up after each test by dropping the collection 
        self.collection.drop()

if __name__ == '__main__':
    unittest.main()