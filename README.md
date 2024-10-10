# CSD-4503-01 
Working on Assignment 2 

Overview:
-> GenZ Gadgets is a simple e-commerce web application built with Flask. It connects to a MongoDB Atlas database to dynamically display product information, including the product's name, tag, price, and image. The application has two routes:
1. Homepage: Provides an introduction to the store.
2. Products Page: Displays a list of products fetched from the MongoDB database.

Features:
1. Dynamic Product Display: Fetches product data from MongoDB Atlas and displays it using Jinja2 templating.
2. Responsive Design: Styled with Bootstrap for mobile-friendly design.
3. Image Handling: Serves product images from a local directory.

Technologies Used:
1. Flask: Python web framework for building the application.
2. MongoDB Atlas: Cloud-hosted NoSQL database to store product information.
3. Jinja2: Template engine for rendering dynamic content.
4. Bootstrap: Frontend framework for responsive and modern design.
5. Pymongo: Python driver for MongoDB to connect and query the database.

To run application:
-> python main.py