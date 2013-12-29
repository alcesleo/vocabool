"""Calls external API:s for translations and definitions, and caches the results to db."""

from vocabool.webservices.adapters import WiktionaryAdapter, YandexTranslateAdapter
from vocabool.domain.models import Definition, Translation

# TODO: if webservice unavailable

class DefinitionRepository():

    def __init__(self, adapter=None):
        """Takes a definition API adapter to use for external calls."""
        if adapter is None:
            adapter = WiktionaryAdapter()

        self.definitions_api = adapter

    def _database_define(self, text, language):
        """Get definition from database."""
        # TODO: return only one?
        definitions = Definition.objects.filter(text=text, language=language)
        if definitions:
            return definitions[0]
        return None

    def _api_define(self, text, language):
        definition = self.definitions_api.define(text, language)

        # TODO: error handling
        if not definition:
            return None

        definition.save()
        return definition


    def get_definition(self, text, language):
        # get from cache
        definition = self._database_define(text, language)
        if not definition:
            definition = self._api_define(text, language)

        return definition


class TranslationRepository():

    def __init__(self, adapter=None):
        if adapter is None:
            adapter = YandexTranslateAdapter()

        self.translation_api = adapter


    def _database_translate(self, text, from_language, to_language):
        """Get translation from DB, returns None if none exist."""
        # get the first object matching, will not throw
        translations = Translation.objects.filter(text=text,
                                                  from_language=from_language,
                                                  to_language=to_language)
        if translations:
            return translations[0]
        return None

    def _api_translate(self, text, from_language, to_language):
        """Get translation from external API."""
        translation = self.translation_api.translate(text, from_language, to_language)

        # TODO: errors
        if not translation:
            return None

        translation.save()
        return translation

    def get_translation(self, text, from_language, to_language):
        """Get translation from database, or fallback to external API."""
        translation = self._database_translate(text, from_language, to_language)
        if not translation:
            translation = self._api_translate(text, from_language, to_language)

        return translation
