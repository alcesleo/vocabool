"""
Attatches appropriate translations and definitions to term-objects,
raises 404 if not successful.
"""

from .repositories import TranslationRepository, DefinitionRepository
from vocabool.settings import SUPPORTED_LANGUAGES
from django.http import Http404

class Service():

    def __init__(self):
        self._translation_repo = None
        self._definition_repo = None

    # lazy initializations

    @property
    def translation_repo(self):
        if self._translation_repo is None:
            self._translation_repo = TranslationRepository()
        return self._translation_repo

    @property
    def definition_repo(self):
        if self._definition_repo is None:
            self._definition_repo = DefinitionRepository()
        return self._definition_repo


    def translate(self, term_obj, to_language):
        """Adds a translation to the passed term object."""
        # validate requested language
        # if to_language not in SUPPORTED_LANGUAGES:
            # TODO: raise bas request, not supported language

        # try to get translation object
        try:
            translation = self.translation_repo.get_translation(term_obj.text, term_obj.language, to_language)
        except Exception, e:
            raise Http404

        term_obj.translations.add(translation)


    def define(self, term_obj):
        """Adds a definition to the passed term object."""
        # try to get definition object
        try:
            definition = self.definition_repo.get_definition(term_obj.text, term_obj.language)
        except Exception, e:
            raise Http404

        term_obj.definitions.add(definition)
