import os
from environs import Env

env = Env()
env.read_env()

host_db = env.str('HOST_DB')
password_db = env.str('PASSWORD_DB')
port_db = env.str('PORT_DB')
name_db = env.str('NAME_DB')
user_db = env.str('USER_DB')
debug_db = env.bool('DEBUG_DB')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': host_db,
        'PORT': port_db,
        'NAME': name_db,
        'USER': user_db,
        'PASSWORD': password_db,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SECRET_KEY')

DEBUG = debug_db

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
