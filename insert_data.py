from pymongo import MongoClient

#Connecting to MongoDB Atlas
client = MongoClient("mongodb+srv://root:R6cc5hdGcljx8FIJ@cluster0.znx2q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db  
products_collection = db.products  

#Some product objects
products = [
    {
        "name": "Vintage Camera",
        "tag": "Exclusive Limited Edition Vintage Camera",
        "price": 99.99,
        "image": "/static/images/camera.jpg"
    },
    {
        "name": "Laptop",
        "tag": "Unbeatable Special Offer on Laptops",
        "price": 130.99,
        "image": "/static/images/msi.jpg"
    },
    {
        "name": "Watch",
        "tag": "Stylish Men's Favorite Smart Watch",
        "price": 259.99,
        "image": "/static/images/watch.jpg"
    },
    {
        "name": "Ipad Pro",
        "tag": "Top Choice for Everyone",
        "price": 1559.99,
        "image": "/static/images/tablet.jpg"
    }
]

prime_day_deals = {
        "name": "Electric Scooter",
        "tag": "Massive Discounts on Electric Scooters",
        "price": 190.99,
        "image": "/static/images/scooter.jpg"
    }

#To add a list of dictionaries into the database
products_collection.insert_many(products)  

#To add a single dictionary into the database
products_collection.insert_one(prime_day_deals)
