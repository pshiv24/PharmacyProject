# PharmacyProject

# Pharmacy Management System

This is a Django-based web application that allows users to manage a pharmacy system. The application provides user authentication and authorization, drug management, order management, and secure RESTful APIs.

## Features

1. **User Authentication and Authorization**
   - Implement endpoints for user registration and login using JWT.
   - Define user roles: Admin and Customer.

2. **Drug Management**
   - Admins can add, update, and delete drug information.
   - Customers can browse drugs.

3. **Order Management**
   - Implement endpoints for customers to place orders.
   - Track and update order status.

4. **RESTful APIs**
   - Ensure all functionalities are accessible via secure RESTful APIs.

5. **Database**
   - Use PostgreSQL for relational data (users, drugs, orders).

6. **Deployment**
   - Deploy the solution on AWS using services like EC2/ECS and RDS.

7. **Code Versioning**
   - Use Git for version control and host the repository on GitHub.
   - Provide clear commit messages and maintain a structured branch strategy.



## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/PharmacyProject.git
cd PharmacyProject


## Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

## Install the required packages:

pip install -r requirements.txt


## Create a PostgreSQL database and user.
Update the DATABASES setting in settings.py with your database credentials.

##Run migrations:
python manage.py makemigrations
python manage.py migrate

## Create a superuser:
python manage.py createsuperuser

##Run the development server:
python manage.py runserver

## Following are the endpoints with examples

## Authentication Endpoints

#Register a new user: 
POST /api/auth/register/

#Obtain JWT token via login: 
POST /api/auth/login/

## Drug Management Endpoints

#List and create drugs: 
GET, POST /api/drugs/

#Update drug: 
PATCH /api/drugs/<int:pk>/update/

#Delete drug: 
DELETE /api/drugs/<int:pk>/delete/

## Order Management Endpoints

#List orders: 
GET /api/orders/

#Update order status: 
PATCH /api/orders/<int:pk>/update/

##Example Data
Users

[
    {
        "username": "admin1",
        "password": "adminpass", // hashed in practice
        "role": "admin"
    },
    {
        "username": "customer1",
        "password": "customerpass", // hashed in practice
        "role": "customer"
    }
]

Drugs

[
    {
        "id": 1,
        "name": "Aspirin",
        "description": "Pain reliever and fever reducer",
        "price": 5.99
    },
    {
        "id": 2,
        "name": "Ibuprofen",
        "description": "Nonsteroidal anti-inflammatory drug (NSAID)",
        "price": 7.99
    },
    {
        "id": 3,
        "name": "Paracetamol",
        "description": "Pain reliever and fever reducer",
        "price": 4.99
    }
]

Orders

[
    {
        "id": 1,
        "username": "customer1",
        "drug_id": 1,
        "quantity": 2,
        "status": "pending"
    },
    {
        "id": 2,
        "username": "customer1",
        "drug_id": 2,
        "quantity": 1,
        "status": "shipped"
    }
]
