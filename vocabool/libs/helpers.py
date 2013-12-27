def ellipsify(str, max_length = 30):
    """Shorten  a long string, adding ellipsis (...)"""
    if len(str) > max_length:
        return str[:max_length] + '...'
    return str


def strip_on_last(char, text, max_length):
    """
    Cuts a string at the latest possible occurence of char that makes the
    text shorter than max_length. If char is not found, returns ''.
    """
    if len(text) < max_length:
        return text

    text = text[:max_length - 1] # if last character is char
    text = text[:text.rfind(char) + 1]
    return text
