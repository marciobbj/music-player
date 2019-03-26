#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn -w 1 -b :8000 api.wsgi api:app