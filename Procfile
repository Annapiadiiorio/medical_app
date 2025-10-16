release: python manage.py migrate
web: python manage.py migrate --noinput && \
     python manage.py collectstatic --noinput && \
     python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'Admin12345')" && \
     gunicorn medical_app.wsgi:application --preload --timeout 120 --log-file -



