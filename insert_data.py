from pymongo import MongoClient

#Connecting to MongoDB Atlas
client = MongoClient("mongodb+srv://root:R6cc5hdGcljx8FIJ@cluster0.znx2q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db  
products_collection = db.products  

#Some product objects
products = [
    {
        "name": "Vintage Camera",
        "tag": "Limiited Edition",
        "price": 99.99,
        "image": "/static/images/camera.jpg"
    },
    {
        "name": "Coffee Beans",
        "tag": "Special Offer",
        "price": 30.99,
        "image": "/static/images/product2.jpg"
    },
    {
        "name": "Lipstick",
        "tag": "Women's Favorite",
        "price": 59.99,
        "image": "/static/images/product3.jpg"
    }
]

prime_day_deals = {
        "name": "Electric Scooter",
        "tag": "Mega Sale",
        "price": 9.99,
        "image": "/static/images/scooter.jpg"
    }

#To add a list of dictionaries into the database
products_collection.insert_many(products)  

#To add a single dictionary into the database
# products_collection.insert_one(prime_day_deals)
