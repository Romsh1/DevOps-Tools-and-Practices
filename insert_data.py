# pip install pymongo
from pymongo import MongoClient

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://root:R6cc5hdGcljx8FIJ@cluster0.znx2q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db  # Replace "app" with your database name
products_collection = db.products  # Replace products with your collection name

# Example product objects
products = [
    {
        "name": "Product 1",
        "tag": "New",
        "price": 29.99,
        "image": "/static/images/product1.jpg"
    },
    {
        "name": "Product 2",
        "tag": "Discounted",
        "price": 49.99,
        "image": "/static/images/product2.jpg"
    },
    {
        "name": "Product 3",
        "tag": "Best Seller",
        "price": 19.99,
        "image": "/static/images/product3.jpg"
    }
]

black_friday_deals = {
        "name": "Product 4",
        "tag": "Black Friday Deals",
        "price": 9.99,
        "image": "/static/images/product4.jpg"
    }

products_collection.insert_many(products)  # allows you to add a list of dictionaries into the database
#products_collection.insert_one(black_friday_deals)  # allows you to add a single dictionary into the database
