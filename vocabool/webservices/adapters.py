"""Parses data from API:s and maps it to domain models."""

from .apis import GoogleDictionaryAPI, YandexTranslateAPI, WiktionaryAPI
from vocabool.domain.models import Definition, Translation

import mwparserfromhell
import re


class WiktionaryAPIAdapter():

    def __init__(self):
        self.definitions = WiktionaryAPI()


    # TODO: error
    def _get_content_string(self, data):
        """The string where the interesting data, among with tons of other junk is."""
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


        # wikicode = mwparserfromhell.parse(content)
        for d in definitions:
            print(d)

        return definitions




    def define(self, text, language):
        data = self.definitions.define(text, language)
        # data = {'query': {'pages': {'14419': {'ns': 0, 'pageid': 14419, 'revisions': [{'*': '{{se även|bajs-}}\n\n==Svenska==\n===Substantiv===\n{{sv-subst-t-oräkn|genitivändelse=|betydelser=1-2.}}\n\'\'\'bajs\'\'\' \'\'n\'\'\n*{{uttal|ipa=bajs}}\n#{{tagg|vardagligt|barnspråk}} [[avföring]]\n#:\'\'Blöjan var full av \'\'\'bajs\'\'\'.\'\'\n#:{{synonymer|[[avföring]], [[faeces]], [[fekalier]], [[exkrementer]], [[skit]], [[spillning]], [[podish]] {{?|hur pass vedertaget?}}}}\n#{{tagg|slang}} [[struntprat]], [[nonsens]], [[skit]]\n#:\'\'Du pratar bara \'\'\'bajs\'\'\'.\'\'\n#(\'\'skolslang från 1930-talet\'\') [[flicka]]\n#{{böjning|sv|subst|baj}}\n:{{avgränsare}}\n:{{besläktade ord|[[baj]], [[baja]], [[bajsa]], [[bajsig]]}}\n\n====Etymologi====\nSedan 1842 av svenska dialektala (Östergötland) \'\'baj\'\' "avföring", vanligt i form uttrycket \'\'fy baj\'\' (jämför [[ajabaja]]), en tillrättavisande term riktat till eller använt av småbarn. Johan Ernst Rietz \'\'Svenskt dialektlexikon\'\' (1962) hänvisar angående \'\'baj\'\' till ett ord ur medelhögtyskan, \'\'baht\'\'.\n\n====Sammansättningar====\n;avföring\n*[[bajshumor]]\n*[[kiss och bajs-humor]]\n*[[bajskorv]]\n*[[bajsnödig]]\n*[[bajsord]]\n*[[bajspåse]]\n*[[hundbajs]]\n\n====Översättningar====\n{{ö-topp}}\n*albanska: {{ö|sq|mut}}, {{ö|sq|jashtëqitje}}\n*bokmål: {{ö+|no|bæsj}}\n*engelska: {{ö+|en|poop}}\n*finska: {{ö+|fi|kakka}}\n*franska: {{ö+|fr|caca}}\n{{ö-mitt}}\n*italienska: {{ö+|it|cacca}}\n*kroatiska: {{ö+|hr|kaka}}\n*polska: {{ö+|pl|kupa}}\n*ryska: {{ö+|ru|какашка|f}}, {{ö+|ru|кака|f}}\n*spanska: {{ö+|es|caca}}\n*tyska: {{ö+|de|Scheiss}}\n{{ö-botten}}\n\n[[en:bajs]]\n[[fr:bajs]]\n[[hu:bajs]]\n[[no:bajs]]\n[[pl:bajs]]\n[[ru:bajs]]', 'contentformat': 'text/x-wiki','contentmodel': 'wikitext'}],'title': 'bajs'}}}}
        print(data)
        print()
        print('-------------- After parsing -----------------')
        print()
        return self._parse_data(data)


class GoogleDictionaryAPIAdapter():

    def __init__(self):
        self.definitions_api = GoogleDictionaryAPI()

    def define(self, text, source_language, target_language):
        data = self.definitions_api.define(
            text, source_language, target_language)

        if not data:
            return None

        definition_text = self._parse_data(data)
        obj = Definition(text=text, language=target_language,
                         definition=definition_text)
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
