from django.db import models
from django.contrib.auth.models import User
from vocabool.libs.helpers import ellipsify

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

CLARIFICATION_CATEGORY = (
    ('def', 'Definition'),
    ('tra', 'Translation'),
    ('syn', 'Synonyms'),
    # ('exp', 'Example'),
)

class Term(models.Model):
    """A term in any language."""
    language = models.CharField(max_length=7, choices=LANGUAGES, default='en')
    text = models.CharField(max_length=100)

    class Meta:
        unique_together = ('text', 'language') # TODO: case insensitive

    def __str__(self):
        return ellipsify(self.text)

class Clarification(models.Model):
    """A {definition, translation, list of synonyms} of a term."""
    term = models.ForeignKey(Term, related_name='clarifications')
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    category = models.CharField(max_length=3, choices=CLARIFICATION_CATEGORY)
    created = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=200)

    # TODO: Provider

    def __str__(self):
        return ellipsify(self.text)

class Listeme(models.Model):
    """
    A term that is owned by a user and belongs to a vocabulary,
    with cherry picked clarifications, and optional custom definition by user.
    """
    owner = models.ForeignKey(User) # TODO: editable=False
    term = models.ForeignKey(Term)
    created = models.DateTimeField(auto_now_add=True)
    clarifications = models.ManyToManyField(Clarification, blank=True)
    custom_text = models.CharField(max_length=200, blank=True)

    # TODO: Validate clarification.term = term

    def __str__(self):
        return self.term.__str__()

class Vocabulary(models.Model):
    """List of listemes, owned by a user."""
    owner = models.ForeignKey(User) # TODO: editable=False
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    listemes = models.ManyToManyField(Listeme, blank=True)

    class Meta:
        verbose_name_plural = 'vocabularies'

    def __str__(self):
        return self.name

    def count(self):
        return self.listemes.count()
