#!/bin/sh
# Wait for environment variables (if needed) and then:
python manage.py collectstatic --noinput
gunicorn learning_platform.wsgi:application --bind 0.0.0.0:8000 --workers 3
