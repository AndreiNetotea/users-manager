# Users manager

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)
[![Mongo Version](https://img.shields.io/badge/mongodb-4.0.3-brightgreen.svg)](https://www.mongodb.com)

### Users manager is a django project with mongodb as database
    Users manages allows you to add, view and delete users.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/AndreiNetotea/users-manager.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


## License

The source code is released under the [MIT License](https://github.com/AndreiNetotea/users-manager/blob/master/LICENSE).