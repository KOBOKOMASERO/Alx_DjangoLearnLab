# API Project

This is a simple Django project demonstrating CRUD operations using **Django REST Framework (DRF)** with token-based authentication.

---

## 🗂 Project Structure

```
api_project/
├── api/                  # Django app containing models, serializers, views
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── api_project/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
└── requirements.txt
```

---

## ⚡ Features

* **Book CRUD API**

  * List all books
  * Retrieve a book by ID
  * Create, update, and delete books
* **Authentication**

  * Token-based authentication using DRF
* **Permissions**

  * Only authenticated users can access API endpoints

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd api_project
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
# venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

6. Run the server:

```bash
python manage.py runserver
```

---

## 📌 API Endpoints

### **Token Authentication**

* Get a token:

```
POST /api/login/
```

Request body:

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

Response:

```json
{
  "token": "your_generated_token"
}
```

Use this token for all authenticated requests:

```
Authorization: Token <your_token_here>
```

---

### **Book CRUD API**

* List all books:

```
GET /api/books_all/
```

* Retrieve a book:

```
GET /api/books_all/<id>/
```

* Create a book:

```
POST /api/books_all/
```

Request body:

```json
{
  "title": "Book Title",
  "author": "Author Name"
}
```

* Update a book:

```
PUT /api/books_all/<id>/
```

* Delete a book:

```
DELETE /api/books_all/<id>/
```

---

### **Optional: Simple List API**

```
GET /api/books/
```

Returns a list of all books without full CRUD.

---

## 🛡 Permissions

* All `books_all` endpoints require authentication
* You can adjust permissions in `api/views.py`:

```python
permission_classes = [IsAuthenticated]  # Only logged-in users
permission_classes = [IsAdminUser]      # Only admins
```

---

## 💡 Notes

* This project uses **DRF’s DefaultRouter** for ViewSets, which automatically generates URLs for CRUD operations.
* Token authentication is implemented using DRF’s built-in `rest_framework.authtoken`.
* You can use **Postman, curl, or your browser** to test the API.

---

## 📚 References

* [Django Documentation](https://docs.djangoproject.com/en/4.2/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* [DRF Token Authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)
