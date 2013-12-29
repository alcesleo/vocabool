"""Attatches appropriate translations and definitions to term-objects."""
from .repositories import TranslationRepository, DefinitionRepository

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
        translation = self.translation_repo.get_translation(term_obj.text, term_obj.language, to_language)
        term_obj.translations.add(translation)


    def define(self, term_obj):
        """Adds a definition to the passed term object."""

        # TODO: 404?
        definition = self.definition_repo.get_definition(term_obj.text, term_obj.language)
        term_obj.definitions.add(definition)
        # term_obj.save()
