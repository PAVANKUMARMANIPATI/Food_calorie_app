#!/bin/bash

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Start the application
echo "Starting application..."
gunicorn calorie_app.wsgi:application
