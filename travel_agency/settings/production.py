import os

from .base import *


DEBUG = False

ALLOWED_HOSTS = [
	host.strip() for host in os.getenv('DJANGO_ALLOWED_HOSTS', '').split(',') if host.strip()
]

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

DATABASES = {
	'default': {
		'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
		'NAME': os.getenv('DB_NAME', ''),
		'USER': os.getenv('DB_USER', ''),
		'PASSWORD': os.getenv('DB_PASSWORD', ''),
		'HOST': os.getenv('DB_HOST', 'localhost'),
		'PORT': os.getenv('DB_PORT', '3306'),
	}
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
