"""
Parses data from API:s and maps it to domain models.
If the content provided by API:s are not satisfying the needs of the models,
a NotFound will be raised, errors thrown by API classes are not handled here.
"""

from .apis import YandexTranslateAPI, WiktionaryAPI
from vocabool.domain.models import Definition, Translation
from vocabool.libs.helpers import strip_on_last
import mwparserfromhell
import re


class NotFound(Exception):
    """Used when there is no content to put in model."""
    pass


class WiktionaryAdapter():

    def __init__(self):
        self.api = WiktionaryAPI()


    # WARNING: A LOT of private parsing methods coming up!


    def _get_content_string(self, data):
        """The string where the interesting data, among with tons of other junk is."""
        # TODO: this should be much nicer
        # empty response
        try:
            for key, value in data['query']['pages'].items():
                return value['revisions'][0]['*']
        except Exception, e:
            raise NotFound


    def _get_relevant_rows(self, content):
        """Get the rows where definitions are placed, without the leading #."""
        # TODO: ignore definitions from other languages
        return re.findall(r'^#([^:*].*?)$', content, re.MULTILINE)


    def _strip_templating(self, text):
        """Removes mediawiki template bullshit and returns readable text."""
        mw = mwparserfromhell.parse(text)
        return mw.strip_code().strip() # strip templates and whitespace


    # TODO: don't hardcode max_length
    def _combine_definitions(self, definitions):
        """
        Place definitions on separate rows, if there are many and/or lengthy
        definitions, only the ones that fit within the max_length will be included.
        """
        return '\n'.join(definitions)


    def _parse_data(self, data):
        """Make sense out of the Mediawiki data."""
        # find the node with the actual content
        content = self._get_content_string(data)

        # find the rows with the definitions
        raw_definitions = self._get_relevant_rows(content)

        # make them readable
        definitions = []
        for d in raw_definitions:
            text = self._strip_templating(d)
            if text:
                definitions.append(text)

        # return string with all definitions on separate rows
        return self._combine_definitions(definitions)



    def define(self, text, language):
        """Get data from Wiktionary as a Definition object."""
        text = text.lower()
        data = self.api.define(text, language)
        definition_text = self._parse_data(data)

        # no definition parsed
        if not definition_text:
            raise NotFound

        return Definition(text=text, language=language, definition=definition_text)


class YandexTranslateAdapter():
    def __init__(self):
        self.api = YandexTranslateAPI()


    def translate(self, text, from_language, to_language):
        """Get data from Yandex Translate as a Translation object."""
        text = text.lower()
        data = self.api.translate(text, from_language, to_language)
        translation_text = self._parse_data(data)

        # no translation
        # (Yandex returns input when not finding a translation, very annoying.)
        if not translation_text or translation_text == text:
            raise NotFound

        translation = Translation(text=text,
                                  from_language=from_language,
                                  to_language=to_language,
                                  translation=translation_text)

        return translation


    def _parse_data(self, data):
        """Place translations on separate rows."""
        return '\n'.join(data['text'])
