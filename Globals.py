import re


class Globals(object):
    """
    @brief This class stores application-level global variables.
    """

    # the scope used to select colors
    color_scope = "text.ass constant.other.color"

    # the regex used to match &HAABBGGRR color codes
    color_abgr_regex_obj = re.compile(
        r"&H(?P<a>[0-9a-f]{2})?(?P<b>[0-9a-f]{2})(?P<g>[0-9a-f]{2})(?P<r>[0-9a-f]{2})\b",
        re.IGNORECASE,
    )
