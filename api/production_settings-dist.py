from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'db_host',
        'PORT': 'db_port',
    }
}

ALLOWED_HOSTS = []

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')