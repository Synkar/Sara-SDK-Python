from urllib.parse import urlencode as _urlencode


def urlencode(params):
    return "?" + _urlencode(params) if params else ""
