import os
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = '$az47@bhkukfu(qn!3cvasdbc-&edrywns7=9sm5b8jhx9ofy-r#'

DEBUG = False

ALLOWED_HOSTS = ['23.102.47.46', '127.0.0.1']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'post_db',
		'USER': 'asist',
		'PASSWORD': '929227007Asdec',
		'HOST': 'localhost',
		'PORT': '5432',
	}
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')