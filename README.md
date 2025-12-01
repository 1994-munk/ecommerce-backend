# 🛒 E-Commerce Backend API  
*A modern, scalable backend built with Django REST Framework, PostgreSQL & JWT Authentication.*

---

## 🚀 Overview
This project is a fully containerized **E-commerce Backend API** designed for real-world production use.  
It includes secure JWT authentication, product management, category organization, and a modular architecture that can scale easily.

---

## 🧩 Features

### 🔐 Authentication
- User Registration  
- User Login  
- JWT Access & Refresh Tokens  
- Protected Routes  
- Token Refresh Endpoint  
- Token Blacklisting for Logout  

### 🛍️ Products
- List Products  
- Create Products  
- View Product Details  
- Filter by Category  

### 🗂️ Categories
- List Categories  
- Create Categories  

---

## 🛠️ Tech Stack
- Django 4+
- Django REST Framework
- SimpleJWT
- PostgreSQL
- Docker & Docker Compose
- Python 3.10+

---

## 📁 Project Structure

```
ecommerce-backend/
│── ecommerce_backend/       # Project settings & config  
│── users/                   # JWT Auth: register, login  
│── products/                # Product API  
│── categories/              # Category API  
│── requirements.txt         # Python dependencies  
│── Dockerfile               # Docker image build  
│── docker-compose.yml       # Docker services  
│── README.md                # Documentation  
```

---

## 🐳 Running the Project with Docker

### 1️⃣ Build and start services  
```bash
docker compose up --build
```

### 2️⃣ Run migrations  
```bash
docker compose exec web python manage.py migrate
```

### 3️⃣ Create superuser (optional)  
```bash
docker compose exec web python manage.py createsuperuser
```

---

## 🔗 API Endpoints

### 🔐 Auth Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/users/register/` | Register new user |
| POST | `/api/users/login/` | Login & get tokens |
| POST | `/api/token/refresh/` | Refresh JWT token |

---

### 🛍️ Product Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/products/` | List all products |
| POST | `/api/products/` | Create a product |
| GET | `/api/products/<id>/` | Product details |

---

### 🗂️ Category Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories/` | List categories |
| POST | `/api/categories/` | Add new category |

---

## 🧪 Example Registration Payload

```json
{
  "username": "",
  "password": "StrongPass123!",
  "email": "name@example.com"
}
```

---

## 🎯 Project Goals
- Build a secure and scalable backend  
- Practice real-world Django REST design patterns  
- Learn JWT authentication deeply  
- Prepare the system for future e-commerce features (cart, orders, payments)

---

## ❤️ Author
Made with love, Python, and lots of caffeine ☕💛  
