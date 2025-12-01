🛒 E-Commerce Backend API

A Django REST Framework + JWT Authentication Powered Backend

📌 Overview

This project is a fully functional e-commerce backend API built using:

Django

Django REST Framework

PostgreSQL

Docker + Docker Compose

JWT Authentication (SimpleJWT)

It provides a clean, modular, and production-ready foundation for building a modern e-commerce system with user accounts, product management, categories, and secure authentication.

🧩 Features
🔐 Authentication

User registration

User login

JWT Access & Refresh tokens

Protected endpoints

Logout by token blacklisting

🛍️ Products

Add products

List products

Filter products by category

Retrieve product details

🧭 Categories

List all categories

Add new categories

🗂️ Project Structure
ecommerce-backend/
│── ecommerce_backend/   # Main project settings
│── users/               # Authentication app
│── products/            # Products CRUD
│── categories/          # Product categories
│── docker/              # Docker config & services
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md

🐳 Running with Docker
1️⃣ Build and Start the Project
docker compose up --build

2️⃣ Run Migrations
docker compose exec web python manage.py migrate

3️⃣ Create Superuser (optional)
docker compose exec web python manage.py createsuperuser

🔗 API Endpoints (Important)
Auth
Method	Endpoint	Description
POST	/api/users/register/	Register new user
POST	/api/users/login/	Login & receive JWT tokens
POST	/api/token/refresh/	Refresh token
Products
Method	Endpoint	Description
GET	/api/products/	List all products
POST	/api/products/	Create a product
GET	/api/products/<id>/	Get product details
Categories
Method	Endpoint	Description
GET	/api/categories/	List categories
POST	/api/categories/	Add new category
🎯 Goals

Build a production-ready e-commerce backend.

Practice Django REST Framework best practices.

Learn JWT-based authentication the correct way.

Create a clean modular architecture suitable for real projects.
