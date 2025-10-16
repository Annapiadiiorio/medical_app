release: python manage.py migrate
web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn medical_app.wsgi:application --preload --timeout 120 --log-file -


