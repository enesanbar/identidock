#!/usr/bin/env bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Running development server..."
    exec python "identidock.py"
elif [ "$ENV" = "UNIT" ]; then
    echo "Running tests..."
    exec python tests.py
else    
    echo "Running production server..."
    exec uwsgi --ini /uwsgi.ini
fi