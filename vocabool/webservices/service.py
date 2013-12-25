"""Returns models from database, or falls back to external API calls."""

from vocabool.webservices.adapters import GoogleDictionaryAPIAdapter, YandexTranslateAPIAdapter
from vocabool.domain.models import Definition, Translation

# TODO: if webservice unavailable

class Service():
    """
    Gets translations and definitions.
    Primarily from database, falls back to external API:s
    """
    def __init__(self, **kwargs):
        # TODO: inject standard apis
        # kwargs['definitions'].setdefault(WikipediaAPI)
        # kwargs['translations'].setdefault(YandexTranslateAPI)

        self.definitions_api = GoogleDictionaryAPIAdapter()
        self.translation_api = YandexTranslateAPIAdapter()

    def _database_define(self, text, language):
        """Get definition from database."""
        definitions = Definition.objects.filter(text=text, language=language)
        if definitions:
            return definitions[0]
        return None

    def _api_define(self, text, language):
        # define in same language
        definition = self.definitions_api.define(text, language, language)

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

    #####################

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
            print('api call made')
            translation = self._api_translate(text, from_language, to_language)

        return translation


### IN API FILE

def definition(text, language):
    definition = service.get_definition(text, language)
    term.definitions.add(definition)
