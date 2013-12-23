from vocabool.webservices.apis import YandexTranslateAPI, GoogleDictionaryAPI
from vocabool.domain.models import Definition, Translation

class Service():
    """
    Gets translations and definitions.
    Primarily from database, falls back to external API:s
    """
    def __init__(self, **kwargs):
        # TODO: inject standard apis
        # kwargs['definitions'].setdefault(WikipediaAPI)
        # kwargs['translations'].setdefault(YandexTranslateAPI)

        self.definitions_api = GoogleDictionaryAPI()
        self.translation_api = YandexTranslateAPI()


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

        # Create and save object to db
        obj = Translation(text=text,
                          from_language=from_language,
                          to_language=to_language,
                          # comma separated if more than one translation is returned
                          translation=', '.join(translation['text']))
        # create object
        obj.save()
        return obj

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
