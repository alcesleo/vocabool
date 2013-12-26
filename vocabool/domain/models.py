from django.db import models
from django.contrib.auth.models import User
from .fields import LanguageField
from vocabool.libs.helpers import ellipsify

# These models are meant to cache results from external API:s, and make them
# easy to filter and search in. They are NOT meant to store the entire wordstock,
# nor are they meant to provide 'links' between translations and terms-definitions.
# From a database design perspective, these are a catastrophe, and they are not
# suited for HUGE amounts of data. They are however very logical and understandable,
# and are very easy to work with. If this app actually gets a ton of users, this
# is where optimizations should be done first.

# TODO: Limit input text lengths

class Definition(models.Model):
    language = LanguageField()
    text = models.CharField(max_length=100)
    definition = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}: {1}'.format(ellipsify(self.text, 10),
                                 ellipsify(self.definition, 10))


class Translation(models.Model):
    from_language = LanguageField()
    to_language = LanguageField()
    text = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}: {1}'.format(ellipsify(self.text),
                                 ellipsify(self.translation))


class Vocabulary(models.Model):
    owner = models.ForeignKey(User)  # TODO: editable=False
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'vocabularies'

    def __str__(self):
        return self.name

    def count(self):
        return self.terms.count()


class Term(models.Model):
    """A term in any language provided by a user."""
    owner = models.ForeignKey(User, related_name='terms')
    vocabulary = models.ForeignKey(Vocabulary, related_name='vocabularies')
    language = LanguageField()
    text = models.CharField(max_length=100)
    custom_text = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    # TODO: limit_choices_to text = self.text
    definitions = models.ManyToManyField(Definition, blank=True)
    translations = models.ManyToManyField(Translation, blank=True)

    def __str__(self):
        return ellipsify(self.text)
