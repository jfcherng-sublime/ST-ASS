from ..helpers.functions import is_my_scope
from typing import Any, Dict, List, Optional, Set, Tuple
import sublime
import sublime_plugin


class AssToggleCommentCommand(sublime_plugin.TextCommand):
    comment_pairs: Tuple[Tuple[str, str], ...] = (
        ("Comment: ", "Dialogue: "),
        ("; ", ""),
    )

    def run(self, edit: sublime.Edit) -> None:
        for comment_point in reversed(self._get_comment_points()):
            for comment_pair in self.comment_pairs:
                comment_pair_found = False
                pre, post = comment_pair

                for _ in range(2):
                    comment_region = sublime.Region(comment_point, comment_point + len(pre))
                    comment_content = self.view.substr(comment_region)

                    if not comment_content.startswith(pre.rstrip()):
                        pre, post = post, pre

                        continue

                    comment_pair_found = True

                    if comment_content != pre:
                        comment_region.b -= len(comment_content) - self._find_first_diff_pos(comment_content, pre)

                    self.view.insert(edit, comment_region.a, post)

                    if not comment_region.empty():
                        self.view.erase(
                            edit,
                            sublime.Region(
                                comment_region.a + len(post),
                                comment_region.b + len(post),
                            ),
                        )

                    break

                if comment_pair_found:
                    break

    def _get_comment_points(self) -> List[int]:
        comment_points: Set[int] = set()
        for region in self.view.sel():
            comment_points |= {
                # the point of first non-space char of the line
                #
                # we do not want to find \r\n
                # because it will make the point belong to the next line
                self.view.find(r"^[ \t]*", line_region.begin()).end()
                for line_region in self.view.lines(region)
            }

        return sorted(comment_points)

    def _find_first_diff_pos(self, str1: str, str2: str) -> int:
        if str1 == str2:
            return -1

        shorter = min(str1, str2, key=len)
        longer = max(str1, str2, key=len)

        shorter_len = len(shorter)
        for i in range(len(longer)):
            if i >= shorter_len or shorter[i] != longer[i]:
                return i

        return shorter_len


class AssToggleCommentEventListener(sublime_plugin.EventListener):
    def on_text_command(
        self,
        view: sublime.View,
        command_name: str,
        args: Dict[str, Any],
    ) -> Optional[Tuple[str, Optional[Dict[str, Any]]]]:
        if command_name != "toggle_comment":
            return None

        # command only works when all target lines are in ASS scope
        check_points: List[int] = []
        for region_selected in view.sel():
            check_points.extend([region.begin() for region in view.lines(region_selected)])

        if all(is_my_scope(view, point) for point in check_points):
            return ("ass_toggle_comment", None)

        return None
