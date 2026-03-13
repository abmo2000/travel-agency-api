from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = True
REDIS_CACHE_URL = 'redis://127.0.0.1:6379/1'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'travel_db',
		'USER': 'laravel_user',
		'PASSWORD': 'password',
		'HOST': 'localhost',
		'PORT': '3306',
	}
}
