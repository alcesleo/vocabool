from django.db import models
from vocabool.settings import SUPPORTED_LANGUAGES

class LanguageField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2)
        kwargs.setdefault('choices', SUPPORTED_LANGUAGES)

        super(LanguageField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"

# make south accept it
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], [r'^vocabool.domain.fields.LanguageField'])
