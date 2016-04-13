Advanced Substation Alpha (ASS) 1.2.0
=====================================

- Add a syntax test file.
- Add scopes for `[]:;,`.


Advanced Substation Alpha (ASS) 1.1.6
=====================================

- Better comment toggling behavior.

  Under the following situation: (chars betweewn """ are selected)

      D"""ialogue: 0,0:00:42.32,0:00:48.84,*Default,,0,0,0,,X
      D"""ialogue: 0,0:00:29.21,0:00:31.19,*Default,,0,0,0,,Y

  Before this patch: (unable to un-comment instantly)

      C"""omment: 0,0:00:42.32,0:00:48.84,*Default,,0,0,0,,X
      """Comment: 0,0:00:29.21,0:00:31.19,*Default,,0,0,0,,Y

  After this patch:

      Comment: """0,0:00:42.32,0:00:48.84,*Default,,0,0,0,,X
      Comment: """0,0:00:29.21,0:00:31.19,*Default,,0,0,0,,Y


Advanced Substation Alpha (ASS) 1.1.5
=====================================

- Use "Comment: /Dialogue: " and "; /" as comment pairs accordingly.


Advanced Substation Alpha (ASS) 1.1.1
=====================================

- Add a changelog message.
- Better auto detection for ASS contents.
- No longer use a strict order to match sections.


Advanced Substation Alpha (ASS) 1.0.0
=====================================

- Initial release.
