"""
WSGI config for studybud project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import time
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root="/static")
# application.add_files("/path/to/more/static/files", prefix="more-files/")
