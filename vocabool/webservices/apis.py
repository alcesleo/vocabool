"""Handles the connection to external API:s."""

import json, requests
from .keys import YANDEX_TRANSLATE_API_KEY # TODO settings.secrets?

# TODO: Shitload of error handling
# TODO: headers = {'User-Agent': 'Vocabool (https://github.com/alcesleo/vocabool; lagginglion@gmail.com)'}
# TODO: URL:ify chars, ' ' to %20

class YandexTranslateAPI():

    def translate(self, text, from_language, to_language):

        base_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        data = "?key={0}&text={1}&lang={2}-{3}".format(
            YANDEX_TRANSLATE_API_KEY,
            text,
            from_language,
            to_language)

        url = base_url + data
        # TODO: if response == input, no translation available?

        # fetch and parse data
        response = requests.get(url)
        data = response.content.decode('utf-8')
        return json.loads(data)

class WiktionaryAPI():
    """
    One of the absolutely best sources of data, has almost everything
    one could want from a dictionary. However, the formatting of the data
    is a murderous demon drenched in hellfire. Good fucking luck parsing it.
    """

    def define(self, text, language):

        # https://www.mediawiki.org/wiki/API
        url = 'http://{lang}.wiktionary.org/w/api.php?format=json&action=query&titles={word}&prop=revisions&rvprop=content'
        url = url.format(lang=language, word=text)

        # TODO: do this on all of them
        response = requests.get(url, headers={'User-Agent': 'Vocabool (https://github.com/alcesleo/vocabool; lagginglion@gmail.com)'})
        data = response.content.decode('utf-8')
        return json.loads(data)


class GoogleDictionaryAPI():
    """
    WARNING: This API is deprecated and has no documentation.
    However it is still one of the most simple dictionary API:s I
    could find, and I'm very happy as long as it works.
    """

    def _jsonp_to_json(self, data):
        """
        Convert jsonp to json,
        removing everything before first {,
        and everything after last }.
        """
        left = data.find('{')
        right = data.rfind('}') + 1
        return data[left:right]

    def define(self, text, source_language, target_language):

        base_url = 'http://www.google.com/dictionary/json'

        # only supports jsonp
        data = '?callback=c&sl={0}&tl={1}&q={2}'.format(source_language, target_language, text)
        url = base_url + data

        response = requests.get(url)
        data = response.content.decode('unicode-escape')
        data = self._jsonp_to_json(data)
        return json.loads(data)

