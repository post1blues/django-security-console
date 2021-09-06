import os
from pathlib import Path
from environs import Env
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'

env = Env()
env.read_env(env_path)

DATABASES = {
    'default': dj_database_url.parse(env("DB_URL"))
}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SECRET_KEY')

DEBUG = env.bool('DEBUG', True)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', ['127.0.0.1', 'localhost'])


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
