Advanced Substation Alpha (ASS) has been updated. To see the changelog, visit
Preferences » Package Settings » Advanced Substation Alpha (ASS) » CHANGELOG


## 2.4.5

- Fix somehow `view.settings().get("syntax", "")` emits error.

  ```
      return bool(view and view.settings().get("syntax", "").endswith("/ASS.sublime-syntax"))
  AttributeError: 'NoneType' object has no attribute 'endswith'
  ```
