from .apis import GoogleDictionaryAPI, YandexTranslateAPI
from vocabool.domain.models import Definition, Translation

# Adapters to the API:s that return domain models directly

class GoogleDictionaryAPIAdapter():

    def __init__(self):
        self.definitions_api = GoogleDictionaryAPI()

    def define(self, text, source_language, target_language):
        data = self.definitions_api.define(text, source_language, target_language)
        if not data:
            return None
        definition_text = self._parse_data(data)
        obj = Definition(text=text, language=target_language, definition=definition_text)
        return obj

    def _parse_data(self, data):
        # FIXME: better parsing
        # TODO: exceptions
        print(data)
        return data['primaries'][0]['entries'][0]['terms'][0]['text']


class YandexTranslateAPIAdapter():

    def __init__(self):
        self.translation_api = YandexTranslateAPI()

    def translate(self, text, from_language, to_language):
        data = self.translation_api.translate(text, from_language, to_language)
        translation_text = self._parse_data(data)
        translation = Translation(text=text,
                         from_language=from_language,
                         to_language=to_language,
                         translation=translation_text)

        return translation

    def _parse_data(self, data):
        """Comma separate multiple translations."""
        return ', '.join(data['text'])

