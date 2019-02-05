"""
This is the module "base64_converter".

This module provides methods that helps converting values
to and from base64 strings.
"""


from datetime import timezone, datetime

_BASE64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789$_'


def _get_timestamp(dt):
    return dt.timestamp() * 1000


def int_to_base64(value):
    """Converts int to base64.
    >>> int_to_base64(1549260000000)
    'Wi3F4sA'
    """
    s = ''
    while value > 0:
        s = _BASE64[value % 64] + s
        value = int(value/64)
    return s


def base64_to_int(s):
    """Converts base64 to int.
    >>> base64_to_int('Wi3F4sA')
    1549260000000
    """
    result = 0
    for char in s:
        value = _BASE64.index(char)
        result *= 64
        result += value
    return result


def datetime_to_base64(dt):
    """Converts datetime to base64.
    >>> datetime_to_base64(datetime(2019, 2, 4, 4, 0, 0))
    'Wi3F4sA'
    """
    ts = int(_get_timestamp(dt))
    return int_to_base64(ts)


def base64_to_datetime(s):
    """Converts base64 to datetime.
    >>> base64_to_datetime('Wi3F4sA')
    datetime.datetime(2019, 2, 4, 4, 0)
    """
    ts = base64_to_int(s) / 1000
    return datetime.fromtimestamp(ts)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
