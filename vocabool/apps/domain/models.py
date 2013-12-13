from django.db import models
from django.contrib.auth.models import User
from vocabool.apps.helpers import ellipsify
from django.conf.global_settings import LANGUAGES # i18n language codes

class Vocabulary(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User) # TODO: editable=False
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'vocabularies'

    def __str__(self):
        return self.name

    # def count items

class Term(models.Model):
    text = models.CharField(max_length=100)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')

    class Meta:
        unique_together = ('text', 'language') # TODO: case insensitive

    def __str__(self):
        return ellipsify(self.text)

class Clarification(models.Model):
    term = models.ForeignKey(Term)
    text = models.CharField(max_length=200)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='en')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ellipsify(self.text)


class Userterm(models.Model):
    vocabulary = models.ForeignKey(Vocabulary)
    term = models.ForeignKey(Term)
    created = models.DateTimeField(auto_now_add=True)
    clarifications = models.ManyToManyField(Clarification)
    custom_text = models.CharField(max_length=200)

    def __str__(self):
        return ellipsify(self.vocabulary.text)
