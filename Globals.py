import re


class Globals(object):
    """
    @brief This class stores application-level global variables.
    """

    color_regex_obj = re.compile(
        r"&H(?P<a>[0-9A-Fa-f]{2})?(?P<b>[0-9A-Fa-f]{2})(?P<g>[0-9A-Fa-f]{2})(?P<r>[0-9A-Fa-f]{2})\b"
    )
