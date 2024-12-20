Sure! Here is the updated `README.md` file without the Docker and Testing sections:

```markdown
# Library Management System

This project is a basic Library Management System API built using Django, Django REST Framework (DRF), and Celery. The system allows users to manage books and authors, handle book borrowing records, and includes a background task for generating periodic reports on library activity.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Running Celery](#running-celery)
- [Contributing](#contributing)
- [License](#license)

## Features

- Manage authors and books.
- Handle book borrowing records.
- Generate periodic reports on library activity using Celery.
- API endpoints for CRUD operations on authors, books, and borrow records.
- Optional bonus features:
  - Error handling and meaningful response messages.
  - Unit tests for selected endpoints.
  - Git version control.
  - API documentation using Swagger or DRF-YASG.
  - User authentication (JWT or session-based) for secured endpoints.

## Prerequisites

- Python 3.6+
- Django 3.0+
- Django REST Framework 3.11+
- Celery 4.4+
- Redis (for Celery broker)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/library_management.git
cd library_management
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run database migrations:

```bash
python manage.py migrate
```

## Usage

1. Start the Django development server:

```bash
python manage.py runserver
```

2. The API will be available at `http://127.0.0.1:8000/api/`.

## API Documentation

API documentation is available using Swagger or DRF-YASG. You can access it at `http://127.0.0.1:8000/api/docs/`.

## Running Celery

1. Start the Redis server (if not already running):

```bash
redis-server
```

2. Start the Celery worker:

```bash
celery -A library_management worker --loglevel=info
```

3. Generate a report by making a POST request to `http://127.0.0.1:8000/api/reports/`.

4. Retrieve the latest report by making a GET request to `http://127.0.0.1:8000/api/reports/`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

This `README.md` file provides a comprehensive guide for setting up, running, and contributing to your Library Management System project, without the Docker and Testing sections.