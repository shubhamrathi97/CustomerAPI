#!/bin/sh

set -e

python manage.py db upgrade

gunicorn -c gunicorn.config.py app:app