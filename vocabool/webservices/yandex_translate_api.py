import json, requests
from .keys import YANDEX_TRANSLATE_API_KEY

def translate(text, from_language, to_language):
    """Translate text using Yandex Translation API."""
    # construct url
    base_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    url = base_url + "?key={0}&text={1}&lang={2}-{3}".format(
        YANDEX_TRANSLATE_API_KEY,
        text,
        from_language,
        to_language)

    # TODO: if response == input, no translation available?

    # fetch and parse data
    response = requests.get(url)
    data = response.content.decode('utf-8')
    return json.loads(data)
