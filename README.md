# My Django Project

This is a Django project for managing your expenses with a REST API and a web interface.

## Features

- **Expense Management**: Add, edit, and delete expenses with descriptions, dates, and values.
- **Category Management**: Create, edit, and delete expense categories (e.g., Food, Transportation).
- **Filtering**: Filter expenses by date range and category.

## Requirements

- Python 3.9+
- Django 3.2+
- PostgreSQL (if you use a database)

## Installation

1. Clone the repository:
   `git clone https://github.com/yourusername/my-django-project.git`

2. Create a virtual environment and activate it:
    `python3 -m venv venv`
    `source venv/bin/activate  # On Windows: venv\Scripts\activate`

3. Install project dependencies:
    `pip install -r requirements.txt`

4. Run the migrations:
    `python manage.py migrate`

5. Start the development server:
    `python manage.py runserver`

Open your web browser and access the application at http://localhost:8000.

## API Endpoints:
    `List Expenses: /api/despesas/`
    `List Categories: /api/categorias/`

For more details on available API endpoints, refer to the project's documentation.