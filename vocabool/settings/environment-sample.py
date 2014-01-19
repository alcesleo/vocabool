#
# Insert your credentials here, and rename this file to `environment.py`.
#

from .general import *
import os

# TODO: SECRET_KEY

DEBUG = True
ALLOWED_HOSTS = ['localhost', 'www.yourdomain.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

USER_AGENT = {
    'User-Agent': 'MyCoolApp (http://myurl.com; myemail@example.com)'
}

YANDEX_TRANSLATE_API_KEY = 'YOUR_YANDEX_TRANSLATE_KEY'
