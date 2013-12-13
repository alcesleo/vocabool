from django.db import models
from django.contrib.auth.models import User
from vocabool.apps.helpers import ellipsify

# significantly reduced version of this list of i18n language codes
# from django.conf.global_settings import LANGUAGES
# https://github.com/django/django/blob/master/django/conf/global_settings.py
from django.utils.translation import gettext_noop
LANGUAGES = (
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

CLARIFICATION_TYPE = (
    ('def', 'Definition'),
    ('tra', 'Translation'),
    ('syn', 'Synonyms'),
)

class Vocabulary(models.Model):
    """List of userterms, owned by a user."""
    owner = models.ForeignKey(User) # TODO: editable=False
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'vocabularies'

    def __str__(self):
        return self.name

    def count(self):
        return self.terms.count()

# TODO: Limit backwards relations with related_name='+' https://docs.djangoproject.com/en/dev/ref/models/fields/

class Term(models.Model):
    """A term in any language."""
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    text = models.CharField(max_length=100)

    class Meta:
        unique_together = ('text', 'language') # TODO: case insensitive

    def __str__(self):
        return ellipsify(self.text)

class Clarification(models.Model):
    """A {definition, translation, list of synonyms} of a term."""
    term = models.ForeignKey(Term)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    clarification_type = models.CharField(max_length=3, choices=CLARIFICATION_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)

    def __str__(self):
        return ellipsify(self.text)


class Userterm(models.Model):
    """
    A term that is owned by a user and belongs to a vocabulary,
    cherry picked clarification, and optional custom definition by user.
    """
    term = models.ForeignKey(Term)
    vocabulary = models.ForeignKey(Vocabulary, related_name='terms')
    created = models.DateTimeField(auto_now_add=True)
    clarifications = models.ManyToManyField(Clarification)
    custom_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return ellipsify(self.term.text)
