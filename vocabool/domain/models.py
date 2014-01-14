from django.db import models
from django.contrib.auth.models import User
from .fields import LanguageField
from vocabool.libs.helpers import ellipsify

# These models are meant to cache results from external API:s, and make them
# easy to filter and search in. They are NOT meant to store the entire wordstock,
# nor are they meant to provide 'links' between translations and terms-definitions.
# From a database design perspective, these are a catastrophe, and they are not
# suited for HUGE amounts of data. They are however very logical and understandable,
# and are very easy to work with.
# The definition and translation-fields can contain multiple definitions, each on their own
# row - since they should be limited, and always displayed together, this has
# not been broken up into separate rows and should be handled later(like surrounding
# each line with p-tags or similar)


class Definition(models.Model):
    language = LanguageField()
    text = models.CharField(max_length=100)
    definition = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0}: {1}'.format(ellipsify(self.text),
                                 ellipsify(self.definition))


class Translation(models.Model):
    from_language = LanguageField()
    to_language = LanguageField()
    text = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{0}: {1}'.format(ellipsify(self.text),
                                 ellipsify(self.translation))


class Vocabulary(models.Model):
    owner = models.ForeignKey(User, related_name='vocabularies')  # TODO: editable=False
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'vocabularies'

    def __unicode__(self):
        return self.name

    def count(self):
        return self.terms.count()


class Term(models.Model):
    """A term in any language provided by a user."""
    owner = models.ForeignKey(User, related_name='terms')
    vocabulary = models.ForeignKey(Vocabulary, related_name='terms')
    language = LanguageField()
    text = models.CharField(max_length=100)
    custom_text = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # TODO: limit_choices_to text = self.text
    definitions = models.ManyToManyField(Definition, blank=True, related_name='terms')
    translations = models.ManyToManyField(Translation, blank=True, related_name='terms')

    class Meta:
        unique_together = ('text', 'language', 'vocabulary')

    def __unicode__(self):
        return ellipsify(self.text)
