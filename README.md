# Django project with TDD • tdd-python-django

This is a Python project built using Django framework built using TDD practices. This README file provides instructions on setting up the project and running various tasks such as creating a virtual environment, running the local development server, managing migrations, and running tests.

## Prerequisites

Before setting up the project, ensure that you have the following prerequisites installed on your system:

- Python 3.11.x _(latest Python 3.11 patch-level)_
- pip package manager

## Installation

1. Clone the project repository:

```shell
   git clone git@github.com:eduardorezaghi/tdd-python-django.git
   cd tdd-python-django
```

2. Create and activate a virtual environment using `virtualenvwrapper`. If you don't have `virtualenvwrapper` installed, you can install it using pip:
```shell
   pip install virtualenvwrapper
```

After the installation completes, you need to configure your shell to work with `virtualenvwrapper`. The configuration involves setting up environment variables and updating your shell's startup file (`~/.bashrc`, `~/.bash_profile`, or `~/.zshrc`, depending on your shell).
* Open the shell's startup file in a text editor:
```shell
   nano ~/.bashrc  # or ~/.bash_profile or ~/.zshrc
```

* Add the following lines at the end of the file:
```shell
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python  # Path to your Python interpreter
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh  # Path to virtualenvwrapper.sh
```
_Note: If the virtualenvwrapper.sh file is located in a different path, adjust the source line accordingly._


Reload the shell's startup file to apply the changes. Run one of the following commands depending on your shell:

For Bash or Zsh:
```shell
source ~/.bashrc  # or ~/.zshrc
```

With the shell reloaded, you should now be able to use virtualenvwrapper commands. Test it by running:
```shell
workon
```
This command should list any existing virtual environments or display an empty list if none exist yet.

3.  Create a virtual environment named `tdd-python-django`:
```shell
   mkvirtualenv tdd-python-django
```

4. Activate the virtual environment:
```shell
   workon tdd-python-django
```
To deactivate the virtual environment and return to your default system environment, execute:

```shell
deactivate
```

5. Install the project dependencies:
```shell
   pip install -r requirements.txt
```

6. Run database migrations:
```shell
   cd superlists/
   python manage.py migrate
```
---
## Usage
### Running the Local Development Server
* To start the local development server, execute the following command:
```shell
   cd superlists/
   python manage.py runserver
```
By default, the server will run on http://localhost:8000/. Open this URL in your web browser to access the application.

### Managing Migrations
Django provides a built-in migration system to manage changes to your database schema. To create and apply new migrations, use the following commands (while being on `superlists/` folder):

* Create a new migration based on the changes you made to your models:

```shell
python manage.py makemigrations
```

* Apply pending migrations to the database:

```shell
python manage.py migrate
```

### Running Tests
This project includes unit and functional tests that can be run either by a manage.py command or by using the functional_tests.py file. To execute the tests, use the following command (while being on `superlists/` folder):
* Unit tests:
```shell
python manage.py tests
```

* Functional (or E2E) tests:
```shell
python functional_tests.py
```
