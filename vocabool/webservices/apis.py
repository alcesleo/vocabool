"""Handles the connection to external API:s."""

import json, requests
from vocabool.settings.credentials import YANDEX_TRANSLATE_API_KEY, USER_AGENT

# TODO: Shitload of error handling
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
