# Spam Identifier API

Spam Identifier API is a Django-based REST API for managing user registrations, contacts, marking numbers as spam, and searching for contacts or spam numbers.

## Features

- User registration and authentication

- Profile management

- Contact management

- Marking phone numbers as spam

- Searching for contacts and spam numbers

## Requirements

- Python 3.x

- Django 3.x or higher

- Django REST Framework

- Django REST Framework SimpleJWT

## Installation

1. **Clone the repository:**
    ```sh
    https://github.com/AmishaSharma12002/Spam_identifier.git
    cd spam_identifier
    ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install the required packages:**
    ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
    ```sh
   python manage.py migrate
   ```

5. **Create a superuser:**
    ```sh
    python manage.py createsuperuser --username admin --email admin@example.com
   # Enter password as Admin when prompted 
   ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### User Endpoints

- **Register a new user:**

    ```sh
    POST /users/register/
    ```
- **Request body:**
    ```json
    {
    "username": "testuser",
    "email": "testuser@example.com",
    "phone_number": "1234567890",
    "password": "testpassword"
    }
    ```

- **Obtain token:**
    ```sh
    POST /users/token/
    ```

- **Request body:**
    ```json
    {
    "username": "testuser",
    "password": "testpassword"
    }
    ```

- **Refresh token:**
    ```sh
    POST /users/token/refresh/
    ```

- **Request body:**
    ```json
    {
    "refresh": "<refresh_token>"
    }
    ```

- **Get user profile (authenticated):**
    ```sh
    GET /users/profile/
    ```

- **Headers:**
    ```sh
    Authorization: Bearer <access_token>
    ```

### Contact Endpoints

- **Get contacts (authenticated):**
    ```sh
    GET /contacts/
    ```

- **Headers:**
    ```sh
    Authorization: Bearer <access_token>
    ```

### Spam Endpoints

- **Mark number as spam (authenticated):**
    ```sh
    POST /spam/mark-spam/
    ```

- **Request body:**
    ```json
    {
    "phone_number": "9876543210"
    }
    ```

- **Headers:**
    ```sh
    Authorization: Bearer <access_token>
    ```

- **Search contacts or spam numbers:**
    ```sh
    GET /spam/search/?query=<search_term>
    ```

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` with the following credentials:

- **Username:** admin

- **Password:** Admin

- **Email:** admin@example.com

