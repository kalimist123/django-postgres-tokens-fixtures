#!/bin/bash
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py sqlmigrate authors 0001_initial
python manage.py migrate
python manage.py loaddata author_fixtures.json

exec "$@"