from .base import *


DEBUG = True

ALLOWED_HOSTS = ['*']

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
