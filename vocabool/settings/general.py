"""
Django settings for vocabool project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1&*)1_0&zavd7)#b6v3gfyp(9ike6%(!!jvv-o*-gsw@o*bwlj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


TEMPLATE_DEBUG = True
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ALLOWED_HOSTS = []


### Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'south',
    'djangobower',
    'jstemplate',
    'pipeline',

    # authentication
    'registration',
    'vocabool.accounts',

    'vocabool.domain',
    'vocabool.client',
    'vocabool.api',
    'vocabool.webservices',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'vocabool.urls'

WSGI_APPLICATION = 'vocabool.wsgi.application'

### Users

LOGIN_REDIRECT_URL = '/app/'


### Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# https://github.com/django/django/blob/master/django/conf/global_settings.py
SUPPORTED_LANGUAGES = (
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('de', 'German'),
    ('el', 'Greek'),
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('hr', 'Croatian'),
    ('hu', 'Hungarian'),
    ('it', 'Italian'),
    ('ru', 'Russian'),
    ('sv', 'Swedish'),
)

### REST configuration

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer', # TODO: Disable this when Debug = False
    ),
    'PAGINATE_BY': 10,                 # Default to 10
    'PAGINATE_BY_PARAM': 'page_size',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100,            # Maximum limit allowed when using `?page_size=xxx
}


### Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'pipeline.finders.PipelineFinder',
)

BOWER_INSTALLED_APPS = (
    'underscore',
    'jquery',
    'jquery.cookie',
    'jquery-timeago',
    'backbone',
    'backbone-pageable',
    'backbone',
    'handlebars',
    'bootstrap',
)


### Static compression

# Make Bower and Pipeline play together
# STATICFILES_DIRS = (
#     os.path.join(BOWER_COMPONENTS_ROOT, 'bower_components'),
# )

STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'bootstrap/dist/css/bootstrap.min.css',
            'client/css/*.css',
        ),
        'output_filename': 'css/main.css',
    },
}


# TODO: Use pipeline for Handlebars files also
# PIPELINE_TEMPLATE_NAMESPACE = 'window.VB.templates'
# PIPELINE_TEMPLATE_EXT = '.html'
# PIPELINE_TEMPLATE_FUNC = 'Handlebars.compile'

# couldn't get yuglify to work with js
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.jsmin.JSMinCompressor'

PIPELINE_JS = {
    'app': {
        'source_filenames': (
            # dependencies
            'underscore/underscore.js',
            'jquery/jquery.js',
            'jquery.cookie/jquery.cookie.js',
            'jquery-timeago/jquery.timeago.js',
            'handlebars/handlebars.js',
            'backbone/backbone.js',
            'backbone-pageable/lib/backbone-pageable.js',
            'bootstrap/dist/js/bootstrap.min.js',

            # FIXME: cannot be globbed since their order matters
            # 'client/js/*.js',

            # application
            'client/js/models.js',
            'client/js/collections.js',
            'client/js/baseviews.js',
            'client/js/views.js',
            'client/js/listviews.js',
            'client/js/controlviews.js',
            'client/js/pageviews.js',
            'client/js/router.js',
            'client/js/helpers.js',
            'client/js/template-helpers.js',
            'client/js/main.js',
        ),
        'output_filename': 'js/app.js'
    }

}

