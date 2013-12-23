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

        self.definitions = GoogleDictionaryAPI()
        self.translations = YandexTranslateAPI()


    def get_translation(self, text, from_language, to_language):
        # get the first object matching, will not throw
        translations = Translation.objects.filter(text=text,
                                              from_language=from_language,
                                              to_language=to_language)
        if translations:
            translation_obj = translation[0]
        else:
            translations = self.translations.translate(text, from_language, to_language)

            # TODO: factory function
            translation_obj = Translation(text=text,
                              from_language=from_language,
                              to_language=to_language,
                              translation=', '.join(translations['text']))
            # create object
            translation_obj.save()

        return translation_obj


### IN API FILE

def definition(text, language):
    definition = service.get_definition(text, language)
    term.definitions.add(definition)
