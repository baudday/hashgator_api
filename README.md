# Installation

In top-most dir
```bash
$ virtualenv venv
$ . venv/bin/activate
$ pip install flask-restful
$ pip install Flask-SQLAlchemy
$ pip install -U marshmallow

# For Postgres support
$ sudo apt-get build-dep python-psycopg2
$ pip install psycopg2 # for postgres support
```

# Run server
```bash
$ python runserver.py
```
