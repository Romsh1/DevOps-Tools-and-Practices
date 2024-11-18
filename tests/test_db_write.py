import unittest
from pymongo import MongoClient
from dotenv import load_dotenv
import os

#Loading environment variables from .env file
load_dotenv()

#Test3
class MongoDBTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        mongo_uri = os.getenv("MONGODB_URI")
        cls.client = MongoClient(mongo_uri)
        cls.db = cls.client['test_db'] 
        cls.collection = cls.db['products']

    def tearDown(self):
        self.collection.delete_many({}) 

    def test_write_data_to_db(self):
        #Test - inserting a new document into MongoDB 
        # -> Expected Output: document should be inserted successfully and be retrievable using a query
        # -> Actual Result: The test will pass if the inserted document is found in the database, and its value matches
        
        #New data to be inserted
        new_data = {"field": "new_value"}

        #Inserting new data into the collection
        self.collection.insert_one(new_data)

        #Quering the database to check if the data was inserted
        inserted_data = self.collection.find_one({"field": "new_value"})

        self.assertIsNotNone(inserted_data)  
        self.assertEqual(inserted_data['field'], 'new_value')  

    @classmethod
    def tearDownClass(cls):
        cls.client.drop_database('test_db')
        cls.client.close()

if __name__ == "__main__":
    unittest.main()