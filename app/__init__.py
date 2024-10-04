from flask import Flask
from pymongo import MongoClient

flask_app = Flask(__name__)

#MongoDB Atlas Connection
client = MongoClient("mongodb+srv://root:R6cc5hdGcljx8FIJ@cluster0.znx2q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db  
products_collection = db.products  

from app import routes