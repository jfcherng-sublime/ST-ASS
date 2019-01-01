import sublime
import sublime_plugin

PLUGIN_NAME = __package__
PLUGIN_DIR = 'Packages/%s' % PLUGIN_NAME


class AssToggleCommentCommand(sublime_plugin.TextCommand):
    commentPairs = [
        ('Comment: ', 'Dialogue: '),
        ('; ', ''),
    ]

    def run(self, edit):
        view = self.view

        for commentPoint in self._getCommentPoints():
            for commentPair in self.commentPairs:
                commentPairFound = False
                pre, post = commentPair

                for _ in range(2):
                    commentRegion = sublime.Region(commentPoint, commentPoint+len(pre))
                    commentContent = view.substr(commentRegion)

                    if not commentContent.startswith(pre.rstrip()):
                        pre, post = post, pre

                        continue

                    commentPairFound = True

                    if commentContent != pre:
                        commentRegion.b -= len(commentContent) - self._findFirstDiffPos(commentContent, pre)

                    view.insert(edit, commentRegion.a, post)

                    if not commentRegion.empty():
                        view.erase(edit, sublime.Region(
                            commentRegion.a + len(post),
                            commentRegion.b + len(post)
                        ))

                    break

                if commentPairFound:
                    return

    def _getCommentPoints(self):
        view = self.view

        commentPoints = set()
        for region in view.sel():
            lineRegions = view.lines(region)

            for lineRegion in lineRegions:
                commentPoint = view.find(r'^\s*', lineRegion.begin()).end()
                commentPoints.add(commentPoint)

        # convert commentPoints into a reversely-sorted list
        return sorted(list(commentPoints), reverse=True)

    def _findFirstDiffPos(self, short, long):
        if short == long:
            return -1

        if len(short) > len(long):
            short, long = long, short

        for i in range(len(long)):
            if i >= len(short) or short[i] != long[i]:
                return i

        return len(short)


class AssToggleCommentEventListener(sublime_plugin.EventListener):
    def on_text_command(self, view, command_name, args):
        if (
            view.settings().get('syntax').startswith(PLUGIN_DIR) and
            command_name == 'toggle_comment'
        ):
            return ('ass_toggle_comment', None)

        return None
