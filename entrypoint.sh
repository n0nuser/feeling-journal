echo "Collect static files\n"
python manage.py collectstatic --no-input

echo "Create database tables\n"
python manage.py makemigrations web --no-input

echo "Apply database migrations\n"
python manage.py migrate --no-input

echo "Create superuser\n"
python manage.py createsuperuser --no-input

echo "Launch Gunicorn (Uvicorn)\n"
gunicorn core.asgi:application --bind :8000 --workers 4 -k uvicorn.workers.UvicornWorker --log-level debug
