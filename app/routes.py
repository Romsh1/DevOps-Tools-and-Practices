from app import flask_app, products_collection
from flask import render_template

@flask_app.route("/")
def index():
    return render_template("home.html")

@flask_app.route("/products")
def products():
    #Fetching all products from MongoDB Atlas
    products = list(products_collection.find())
    print(products)
    return render_template("products.html", products=products)
