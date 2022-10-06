#!/bin/sh
python3 manage.py makemigrations API
python3 manage.py migrate
