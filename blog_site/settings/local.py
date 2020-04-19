from .base import *


DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'saper663emailbot@gmail.com'
EMAIL_HOST_PASSWORD = 'gjxnjdsq<jn'
EMAIL_PORT = 587
EMAIL_USE_TLS = True