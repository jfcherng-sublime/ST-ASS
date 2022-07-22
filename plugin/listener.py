from typing import Any, Dict, Optional, Tuple

import sublime
import sublime_plugin

from .functions import is_my_scope, is_my_syntax


class AssToggleCommentEventListener(sublime_plugin.EventListener):
    def on_text_command(
        self,
        view: sublime.View,
        command_name: str,
        args: Dict[str, Any],
    ) -> Optional[Tuple[str, Optional[Dict[str, Any]]]]:
        if command_name != "toggle_comment":
            return None

        if is_my_syntax(view):
            return ("ass_toggle_comment", None)

        # command only works when all target lines are in ASS scope
        if not all(
            # ...
            is_my_scope(view, line.begin())
            for sel_region in view.sel()
            for line in view.lines(sel_region)
        ):
            return None
        return ("ass_toggle_comment", None)
