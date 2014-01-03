"""
WSGI config for PythonAnywhere using Python2.7 in a virtualenv.
https://www.pythonanywhere.com/wiki/VirtualEnvForNewerDjango
"""

# activate virtualenv
activate_this = '/home/alcesleo/.virtualenvs/vocabool2/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

path = '/home/alcesleo/vocabool'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'vocabool.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
