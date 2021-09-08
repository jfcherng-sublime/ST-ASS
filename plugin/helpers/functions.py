import sublime


def is_my_syntax(view: sublime.View) -> bool:
    if not view:
        return False

    syntax = view.settings().get("syntax")

    if not isinstance(syntax, str):
        return False

    return syntax.endswith("/ASS.sublime-syntax")


def is_my_scope(view: sublime.View, point: int) -> bool:
    return view.match_selector(point, "text.ass")
