from typing import List, Set, Tuple

import sublime
import sublime_plugin

ASS_COMMENT_PAIRS: Tuple[Tuple[str, str], ...] = (
    # (before_command_executed, after_command_executed),
    ("Comment: ", "Dialogue: "),
    ("Dialogue: ", "Comment: "),
    ("; ", ""),
    ("", "; "),  # always matches
)


def find_first_diff_pos(str1: str, str2: str) -> int:
    """Finds the first difference position. Returns `-1` if both strings are identical."""
    if str1 == str2:
        return -1

    shorter, longer = sorted((str1, str2), key=len)
    shorter_len = len(shorter)

    return next(
        (i for i in range(shorter_len) if shorter[i] != longer[i]),
        shorter_len,
    )


def get_caret_line_beginning_points(view: sublime.View) -> List[int]:
    """Gets the points of the first non-space char of the caret lines."""
    points: Set[int] = set()
    for region in view.sel():
        points |= {view.find(r"^[ \t]*", line_region.begin()).end() for line_region in view.lines(region)}
    return sorted(points)


class AssToggleCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit: sublime.Edit) -> None:
        for beginning_point in reversed(get_caret_line_beginning_points(self.view)):
            for before, after in ASS_COMMENT_PAIRS:
                comment_region = sublime.Region(beginning_point, beginning_point + len(before))
                comment_content = self.view.substr(comment_region)
                if not comment_content.startswith(before.rstrip()):
                    continue

                if comment_content != before:
                    comment_region.b -= len(comment_content) - find_first_diff_pos(comment_content, before)

                self.view.insert(edit, comment_region.a, after)
                self.view.erase(
                    edit,
                    sublime.Region(
                        comment_region.a + len(after),
                        comment_region.b + len(after),
                    ),
                )
                break
