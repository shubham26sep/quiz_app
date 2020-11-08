GAMES App
=========

# Installation

## Virtual Envirnoment and requirements

    virtualenv -p /path/to/python3.6 venv
    source venv/bin/activate
    pip install -r requirements.txt

## Postgres setup

    pip install mysqlclient

    -In MySQL Shell
    CREATE DATABASE db_name;

## Add mysql database settings in DATABASE settings in config/local.py

## Create a superuser account.

    python manage.py createsuperuser

## Running Development Server

    python manage.py runserver

**Note:** Never forget to enable virtual environment (`source venv/bin/activate`) before running above command and use settings accordingly.
