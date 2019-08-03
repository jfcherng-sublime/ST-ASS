import bisect
import sublime


def find_color_regions_by_region(view: sublime.View, region) -> list:
    """
    @brief Found intersected color regions from view by region

    @param view   The view
    @param region The region

    @return list[] Found color regions
    """

    view_color_regions = view_color_regions_val(view)

    if not view_color_regions:
        return []

    region = region_into_list_form(region, True)

    # since "view_color_regions" is auto sorted, we could perform a binary searching
    insert_idx = bisect.bisect_left(view_color_regions, region)

    # at most, there are 3 color regions that are possibly intersected with "region"
    possible_idxs = filter(
        # fmt: off
        lambda idx: 0 <= idx < len(view_color_regions),
        [insert_idx - 1, insert_idx, insert_idx + 1]
        # fmt: on
    )

    return [
        view_color_regions[idx]
        for idx in possible_idxs
        if is_intersected(view_color_regions[idx], region, True)
    ]


def find_color_regions_by_regions(view: sublime.View, regions: list) -> list:
    """
    @brief Found intersected color regions from view by regions

    @param view    The view
    @param regions The regions

    @return list[] Found color regions
    """

    color_regions = []
    for region in regions:
        color_regions.extend(find_color_regions_by_region(view, region))
    color_regions.sort()

    # remove duplicated regions
    return [
        color_regions[idx]
        for idx in range(len(color_regions))
        if idx == 0 or color_regions[idx] != color_regions[idx - 1]
    ]


def view_find_all_fast(view: sublime.View, regex_obj, return_st_region: bool = True) -> list:
    """
    @brief A faster/simpler implementation of View.find_all().

    @param view             the View object
    @param regex_obj        the compiled regex object
    @param return_st_region return region in sublime.Region type

    @return sublime.Region[]|list[]
    """

    iterator = regex_obj.finditer(view.substr(sublime.Region(0, view.size())))
    regions = [m.span() for m in iterator] if iterator else []

    if return_st_region:
        regions = [sublime.Region(*r) for r in regions]

    return regions


def view_update_color_regions(view: sublime.View, color_scope: str) -> list:
    """
    @brief Update view's "color_regions" variable

    @param view        The view
    @param color_scope The scope used to select colors

    @return the new "color_regions" in the view
    """

    color_regions = view.find_by_selector(color_scope)

    view_color_regions_val(view, color_regions)

    return color_regions


def view_color_regions_val(view: sublime.View, color_regions=None):
    """
    @brief Set/Get the color regions (in list of lists) of the current view

    @param view          The view
    @param color_regions The color regions (None = get mode, otherwise = set mode)

    @return None|list[] None if the set mode, otherwise the color regions
    """

    if color_regions is None:
        return view.settings().get("ASS_color_regions", [])

    color_regions = [region_into_list_form(r, True) for r in color_regions]

    view.settings().set("ASS_color_regions", color_regions)


def view_typing_timestamp_val(view: sublime.View, timestamp_s=None):
    """
    @brief Set/Get the color regions (in list of lists) of the current view

    @param view        The view
    @param timestamp_s The last timestamp (in sec) when the user is typing

    @return None|float None if the set mode, otherwise the value
    """

    if timestamp_s is None:
        return view.settings().get("ASS_typing_timestamp", False)

    view.settings().set("ASS_typing_timestamp", timestamp_s)


def region_into_list_form(region, sort_result: bool = False) -> list:
    """
    @brief Convert the "region" into list form

    @param region      The region
    @param sort_result Sort the region

    @return list the "region" into list form
    """

    if isinstance(region, sublime.Region):
        region = [region.a, region.b]
    elif isinstance(region, int) or isinstance(region, float):
        region = [int(region)] * 2
    elif hasattr(region, "__iter__") and not isinstance(region, list):
        region = list(region)

    assert isinstance(region, list)

    if not region:
        raise ValueError("region must not be empty.")

    if len(region) == 1:
        region *= 2
    elif len(region) > 2:
        region = region[0:2]

    return sorted(region) if sort_result else region


def is_intersected(region_1, region_2, allow_pointy_boundary: bool = False) -> bool:
    """
    @brief Check whether two regions are intersected.

    @param region_1              The 1st region
    @param region_2              The 2nd region
    @param allow_pointy_boundary Treat pointy boundary as intersected

    @return True if intersected, False otherwise.
    """

    # left/right begin/end = l/r b/e
    lb, le = region_into_list_form(region_1, True)
    rb, re = region_into_list_form(region_2, True)

    # one of the region is actually a point and it's on the other region's boundary
    if allow_pointy_boundary and (
        lb == rb == re or le == rb == re or rb == lb == le or re == lb == le
    ):
        return True

    return (
        (lb == rb and le == re)
        or (rb > lb and rb < le)
        or (re > lb and re < le)
        or (lb > rb and lb < re)
        or (le > rb and le < re)
    )


def is_my_syntax() -> bool:
    return (
        sublime.active_window()
        .active_view()
        .settings()
        .get("syntax")
        .endswith("/ASS.sublime-syntax")
    )


def is_my_scope(point: int) -> bool:
    return sublime.active_window().active_view().match_selector(point, "text.ass")


def hex_to_rgba(color_hex: str, alpha="FF"):
    """
    @brief Convert hex color string into int dict

    @param color_hex The hex color string
    @param alpha     The alpha. Can be string (00~FF) or int (0~255)

    @return An int dict containing each color components
    """

    color_hex_len = len(color_hex)

    if color_hex_len != 3 and color_hex_len != 6:
        return None

    if isinstance(alpha, str):
        alpha = int(alpha, 16)

    alpha = max(0, min(255, alpha))
    a = 1 - alpha / 0xFF

    # extend 3-char RGB to 6-char
    if color_hex_len == 3:
        color_hex = color_hex[0] * 2 + color_hex[1] * 2 + color_hex[2] * 2

    # split RGB
    r, g, b = [color_hex[i : i + 2] for i in range(0, len(color_hex), 2)]

    # RGB hex to int
    r, g, b = [int(val, 16) for val in (r, g, b)]

    return {"r": r, "g": g, "b": b, "a": a}
