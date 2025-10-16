"""
WSGI config for medical_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medical_app.settings')

application = get_wsgi_application()
# Esegui automaticamente le migrations su Render (solo se necessario)
import os
from django.core.management import call_command
from django.db import OperationalError

try:
    call_command('migrate', interactive=False)
except OperationalError:
    print("⚠️  Database non pronto, skip migrations.")

