import sublime
import sublime_plugin

PLUGIN_NAME = __package__
PLUGIN_DIR = "Packages/%s" % PLUGIN_NAME
PLUGIN_SETTINGS = "%s.sublime-settings" % PLUGIN_NAME


class AssToggleCommentCommand(sublime_plugin.TextCommand):
    # fmt: off
    comment_pairs = [
        ("Comment: ", "Dialogue: "),
        ("; ", ""),
    ]
    # fmt: on

    def run(self, edit: sublime.Edit) -> None:
        v = self.view

        for comment_point in self._get_comment_points():
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
                        v.erase(
                            edit,
                            # fmt: off
                            sublime.Region(
                                comment_region.a + len(post),
                                comment_region.b + len(post),
                            ),
                            # fmt: on
                        )

                    break

                if comment_pair_found:
                    return

    def _get_comment_points(self) -> list:
        v = self.view

        comment_points = set()
        for region in v.sel():
            line_regions = v.lines(region)

            for line_region in line_regions:
                comment_point = v.find(r"^\s*", line_region.begin()).end()
                comment_points.add(comment_point)

        # convert comment_points into a reversely-sorted list
        return sorted(list(comment_points), reverse=True)

    def _find_first_diff_pos(self, shorter: str, longer: str) -> int:
        if shorter == longer:
            return -1

        if len(shorter) > len(longer):
            shorter, longer = longer, shorter

        for i in range(len(longer)):
            if i >= len(shorter) or shorter[i] != longer[i]:
                return i

        return len(shorter)


class AssToggleCommentEventListener(sublime_plugin.EventListener):
    def on_text_command(self, view: sublime.View, command_name: str, args: dict):
        if (
            view.settings().get("syntax").startswith(PLUGIN_DIR)
            and command_name == "toggle_comment"
        ):
            return ("ass_toggle_comment", None)

        return None
