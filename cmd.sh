#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    exec python "identidock.py"
else
    echo "Running Production Server"
    exec uwsgi --ini /uwsgi.ini
fi