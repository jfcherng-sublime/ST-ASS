import sublime


def is_my_syntax(view: sublime.View) -> bool:
    return syntax.scope == "text.ass" if (syntax := view.syntax()) else False


def is_my_scope(view: sublime.View, point: int) -> bool:
    return view.match_selector(point, "text.ass")
