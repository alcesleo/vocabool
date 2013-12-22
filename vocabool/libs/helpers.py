def ellipsify(str, max_length = 30):
    """Shorten  a long string, adding ellipsis (...)"""
    if len(str) > max_length:
        return str[:max_length] + '...'
    return str
