from django.db import models
from django.contrib.auth.models import User
from vocabool.apps.helpers import ellipsify

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
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, default='en') # ISO 639-1 language code

    class Meta:
        unique_together = ('text', 'language') # TODO: case insensitive

    def __str__(self):
        return ellipsify(self.text)

class Clarification(models.Model):
    term = models.ForeignKey(Term)
    text = models.CharField(max_length=200)
    language = models.CharField(max_length=2)

    def __str__(self):
        return ellipsify(self.text)


class UserTerm(models.Model):
    vocabulary = models.ForeignKey(Vocabulary)
    term = models.ForeignKey(Term)
    created = models.DateTimeField(auto_now_add=True)
    clarifications = models.ManyToManyField(Clarification)
    custom_text = models.CharField(max_length=200)

    def __str__(self):
        return ellipsify(self.vocabulary.text)
