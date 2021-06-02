#!/bin/bash

cd /usr/src/app
python manage.py makemigrations
python manage.py migrate

echo "Running server"
pip install -r requirements.txt

python manage.py runserver 0.0.0.0:8000 --insecure
