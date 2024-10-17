# CSD-4503-01 
Working on Assignment 2 (Continued...)

-> GenZ Gadgets is a simple e-commerce web application built with Flask. It connects to a MongoDB Atlas database to dynamically display product information, including the product's name, tag, price, and image. The app features two main routes for navigation: the Homepage and the Products Page. It also implements secure configuration management by utilizing environment variables with .env files and GitHub Secrets.

-> Features
1. Dynamic Product Display:
Fetches product data from MongoDB Atlas and displays it dynamically using Jinja2 templates.
Displays the product's name, tag, price, and image on the products page.
2. Secure Configuration Management:
Uses .env files to store sensitive information like database credentials securely.
Implements GitHub Secrets to manage these variables during deployment, ensuring that sensitive information is not exposed in the source code.
3. Responsive Design:
Styled with Bootstrap to provide a mobile-friendly design and ensure that the site looks good on all screen sizes.
4. Image Handling:
Serves product images from a local directory for efficient and secure handling of images.
5. Cloud-Hosted Database:
Utilizes MongoDB Atlas, a cloud-based NoSQL database, for storing and retrieving product information.

-> Technologies Used
1. Flask: Python web framework used to build the web application.
2. MongoDB Atlas: Cloud-hosted NoSQL database for storing product information.
3. Pymongo: Python driver to connect and interact with MongoDB.
4. Jinja2: Templating engine for rendering dynamic content within the application.
5. Bootstrap: CSS framework for creating a responsive and modern design.
6. GitHub Secrets: Used for securely storing sensitive environment variables during deployment.

To run application:
-> python main.py