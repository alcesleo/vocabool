"""
Handles the connection to external API:s.
They are made with User-Agent headers from settings, and use requests' errors:
http://docs.python-requests.org/en/latest/user/quickstart/#errors-and-exceptions.
"""


import json, requests
from vocabool.settings import YANDEX_TRANSLATE_API_KEY, USER_AGENT


class APIBase():
    """Sends requests to API:s with correct user-agent headers and exceptions."""

    def _get_json_data(self, url):
        """Get json from external url and return object."""
        # make request
        response = requests.get(url, headers=USER_AGENT)
        response.raise_for_status() # throw on non-ok response codes

        # parse result
        return json.loads(response.text)


class YandexTranslateAPI(APIBase):

    def translate(self, text, from_language, to_language):

        base_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        data = "?key={0}&text={1}&lang={2}-{3}".format(
            YANDEX_TRANSLATE_API_KEY,
            text,
            from_language,
            to_language)

        url = base_url + data

        # fetch and parse data
        return self._get_json_data(url)


class WiktionaryAPI(APIBase):
    """
    One of the absolutely best sources of data, has almost everything
    one could want from a dictionary. However, the formatting of the data
    is a murderous demon drenched in hellfire. Good fucking luck parsing it.
    """

    def define(self, text, language):

        # https://www.mediawiki.org/wiki/API
        url = 'http://{lang}.wiktionary.org/w/api.php?format=json&action=query&titles={word}&prop=revisions&rvprop=content'
        url = url.format(lang=language, word=text)

        return self._get_json_data(url)
