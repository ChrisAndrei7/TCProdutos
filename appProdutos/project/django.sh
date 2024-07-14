#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations produtos
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Starting Server..."
python manage.py runserver 3.92.215.255:8003
