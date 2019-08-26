from .settings import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

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

CORS_ORIGIN_WHITELIST = []

SENTRY_SDK_KEY = ''

# Set sentry sdk key here
sentry_sdk.init(
    dsn=SENTRY_SDK_KEY,
    integrations=[DjangoIntegration()]
)