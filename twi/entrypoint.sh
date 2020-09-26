#!/bin/sh

echo "Start --> Django Migrate"
python manage.py migrate --noinput
echo "Start --> Django Collect Static Files"
python manage.py collectstatic --no-input --clear

exec "$@"