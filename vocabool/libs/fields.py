from django.db import models
from django.utils.translation import gettext_noop

# significantly reduced version of this list of i18n language codes
# from django.conf.global_settings import LANGUAGES
# https://github.com/django/django/blob/master/django/conf/global_settings.py
LANGUAGES = (
    ('-', gettext_noop('Not provided')),
    ('cs', gettext_noop('Czech')),
    ('da', gettext_noop('Danish')),
    ('de', gettext_noop('German')),
    ('el', gettext_noop('Greek')),
    ('en', gettext_noop('English')),
    ('en-gb', gettext_noop('British English')),
    ('es', gettext_noop('Spanish')),
    ('fa', gettext_noop('Persian')),
    ('fi', gettext_noop('Finnish')),
    ('fr', gettext_noop('French')),
    ('hr', gettext_noop('Croatian')),
    ('hu', gettext_noop('Hungarian')),
    ('it', gettext_noop('Italian')),
    ('ru', gettext_noop('Russian')),
    ('sv', gettext_noop('Swedish')),
)

class LanguageField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        kwargs.setdefault('choices', LANGUAGES)

        super(LanguageField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"
