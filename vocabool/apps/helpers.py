
def ellipsify(str, max_length = 30):
    """Shorten long strings adding ellipsis (...)"""
    if len(str) > max_length:
        return str[:max_length] + '...'
    return str
