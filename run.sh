#!/bin/bash

python3 ./kanban/manage.py makemigrations
python3 ./kanban/manage.py migrate
python3 ./kanban/create_user.py

gunicorn -c etc/gunicorn.py --pythonpath $(pwd)/kanban kanban.wsgi:application
