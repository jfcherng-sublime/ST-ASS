import sublime
import sublime_plugin
from .functions import is_my_scope


class AssToggleCommentCommand(sublime_plugin.TextCommand):
    # fmt: off
    comment_pairs = [
        ("Comment: ", "Dialogue: "),
        ("; ", ""),
    ]
    # fmt: on

    def run(self, edit: sublime.Edit) -> None:
        v = self.view

        for comment_point in reversed(self._get_comment_points()):
            for comment_pair in self.comment_pairs:
                comment_pair_found = False
                pre, post = comment_pair

                for _ in range(2):
                    comment_region = sublime.Region(comment_point, comment_point + len(pre))
                    comment_content = v.substr(comment_region)

                    if not comment_content.startswith(pre.rstrip()):
                        pre, post = post, pre

                        continue

                    comment_pair_found = True

                    if comment_content != pre:
                        # fmt: off
                        comment_region.b -= (
                            len(comment_content)
                            - self._find_first_diff_pos(comment_content, pre)
                        )
                        # fmt: on

                    v.insert(edit, comment_region.a, post)

                    if not comment_region.empty():
                        # fmt: off
                        v.erase(edit, sublime.Region(
                            comment_region.a + len(post),
                            comment_region.b + len(post),
                        ))
                        # fmt: on

                    break

                if comment_pair_found:
                    break

    def _get_comment_points(self) -> list:
        v = self.view

        comment_points = set()
        for region in v.sel():
            # fmt: off
            comment_points |= {
                # the point of first non-space char of the line
                #
                # we do not want to find \r\n
                # because it will make the point belong to the next line
                v.find(r"^[ \t]*", line_region.begin()).end()
                for line_region in v.lines(region)
            }
            # fmt: on

        return sorted(list(comment_points))

    def _find_first_diff_pos(self, str1: str, str2: str) -> int:
        if str1 == str2:
            return -1

        shorter = min(str1, str2, key=len)
        longer = max(str1, str2, key=len)

        shorterLen = len(shorter)
        for i in range(len(longer)):
            if i >= shorterLen or shorter[i] != longer[i]:
                return i

        return shorterLen


class AssToggleCommentEventListener(sublime_plugin.EventListener):
    def on_text_command(self, view: sublime.View, command_name: str, args: dict):
        if command_name != "toggle_comment":
            return None

        # command only works when all target lines are in ASS scope
        check_points = []
        for region_selected in view.sel():
            check_points.extend([region.begin() for region in view.lines(region_selected)])

        if all(is_my_scope(point) for point in check_points):
            return ("ass_toggle_comment", None)
