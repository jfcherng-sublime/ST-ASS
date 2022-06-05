# Advanced Substation Alpha (ASS) Changelog

## 4.0.2

- feat: add scope for newline after section end

## 4.0.1

- fix: modules should be reloaded when update plugin
- refactor: simplify `boot.py`

## 4.0.0

- Remove built-in color codes visualization support.

  Because as of [ColorHelper](https://packagecontrol.io/packages/ColorHelper) 3.6.0,
  it provides support for ASS/SSA color codes. And ColorHelper's functionality is superior
  to this plugin's built-in. Thus, ColorHelper is recommended if you need color codes visualization.

## 3.0.0

- Drop support for ST 3

  There is another a legacy branch for ST 3.

## 2.5.2

- Fix wrong settings filename

## 2.5.1

- Just some internal refactoring

## 2.5.0

- Plugin runs on Python 3.8 if ST 4

## 2.4.5

- Fix somehow `view.settings().get("syntax", "")` emits error.

  ```text
  return bool(view and view.settings().get("syntax", "").endswith("/ASS.sublime-syntax"))
  AttributeError: 'NoneType' object has no attribute 'endswith'
  ```

## 2.4.4

- Fix somehow sometimes `view.settings().get("syntax")` returns `None`.

## 2.4.3

- Fix exception when opening an image.

## 2.4.2

- Remove font/actor name from the symbol list.

## 2.4.1

- Find color regions by selector rather than by regex.

## 2.4.0

- Update color box template to show both opaque/alpha colors.

## 2.3.3

- Fix comment command does not work across lines.
- Comment command works depending on the scope rather than the syntax.

## 2.3.2

- Fix color code detection should only be done in ASS/SSA syntax.
- Change default "on_modified_typing_period" to 150.

## 2.3.1

- Regex should not match malformed color codes.

## 2.3.0

- Add the ability to open plugin settings from the main menu.
- Revert "Fix settings file is not found." from `2.2.1` (false alarm).

## 2.2.1

- Fix settings file is not found.

## 2.2.0

- Add the ability to visualize color via inline phantoms.

## 2.1.0

- Add `Symbol List.tmPreferences`.

## 2.0.1

- Fix highlighting of special chars. (@FichteFoll)

## 2.0.0

- This is a full re-write done by @FichteFoll. Thank you!

## 1.2.1

- Just some directory structure tweaks.

## 1.2.0

- Add a syntax test file.
- Add scopes for `[]:;,`.

## 1.1.6

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

## 1.1.5

- Use "Comment: /Dialogue: " and "; /" as comment pairs accordingly.

## 1.1.1

- Add a changelog message.
- Better auto detection for ASS contents.
- No longer use a strict order to match sections.

## 1.0.0

- Initial release.
