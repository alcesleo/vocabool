"""Parses data from API:s and maps it to domain models."""

from .apis import YandexTranslateAPI, WiktionaryAPI
from vocabool.domain.models import Definition, Translation
from vocabool.libs.helpers import strip_on_last
import mwparserfromhell
import re

# TODO: if not found

class WiktionaryAdapter():

    def __init__(self):
        self.api = WiktionaryAPI()


    # WARNING: A LOT of private parsing methods coming up!


    def _get_content_string(self, data):
        """The string where the interesting data, among with tons of other junk is."""
        # TODO: error handling
        for key, value in data['query']['pages'].items():
            return value['revisions'][0]['*']


    def _get_relevant_rows(self, content):
        """Get the rows where definitions are placed, without the leading #."""
        # TODO: ignore definitions from other languages
        return re.findall(r'^#([^:*].*?)$', content, re.MULTILINE)


    def _strip_templating(self, text):
        """Removes mediawiki template bullshit and returns readable text."""
        mw = mwparserfromhell.parse(text)
        return mw.strip_code().strip() # strip templates and whitespace


    def _combine_definitions(self, definitions, max_length=300):
        """
        Place definitions on separate rows, if there are many and/or lengthy
        definitions, only the ones that fit within the max_length will be included.
        """
        text = '\n'.join(definitions)
        return strip_on_last('\n', text, max_length)



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
        data = self.api.define(text, language)
        definition_text = self._parse_data(data)
        return Definition(text=text, language=language, definition=definition_text)


class YandexTranslateAdapter():
    def __init__(self):
        self.api = YandexTranslateAPI()


    def translate(self, text, from_language, to_language):
        """Get data from Yandex Translate as a Translation object."""
        data = self.api.translate(text, from_language, to_language)
        translation_text = self._parse_data(data)
        translation = Translation(text=text,
                                  from_language=from_language,
                                  to_language=to_language,
                                  translation=translation_text)

        return translation


    def _parse_data(self, data):
        """Place translations on separate rows."""
        return '\n'.join(data['text'])
