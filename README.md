# Django project with TDD • tdd-python-django

This is a Python project built using Django framework built using TDD practices. This README file provides instructions on setting up the project and running various tasks such as creating a virtual environment, running the local development server, managing migrations, and running tests.

## Prerequisites

Before setting up the project, ensure that you have the following prerequisites installed on your system:

- Python 3.x
- pip package manager

## Installation

1. Clone the project repository:

```shell
   git clone <repository-url>
   cd superlists
```

2. Create and activate a virtual environment using virtualenvwrapper. If you don't have virtualenvwrapper installed, you can install it using pip:
* Create a virtual environment named `superlists`:
```shell
   mkvirtualenv superlists
```

* Activate the virtual environment:
```shell
   workon superlists
```

3. Install the project dependencies:
```shell
   pip install -r requirements.txt
```

4. Run database migrations:
```shell
   python manage.py migrate
```
---
## Usage
### Running the Local Development Server
* To start the local development server, execute the following command:
```shell
   python manage.py runserver
```
By default, the server will run on http://localhost:8000/. Open this URL in your web browser to access the application.

### Managing Migrations
Django provides a built-in migration system to manage changes to your database schema. To create and apply new migrations, use the following commands:

* Create a new migration based on the changes you made to your models:

```shell
python manage.py makemigrations
```

* Apply pending migrations to the database:

```shell
python manage.py migrate
```

### Running Tests
This project includes functional tests that can be run using the functional_tests.py file. To execute the tests, use the following command:

```shell
python functional_tests.py
```

This command will run the functional tests and display the test results in the console.