Sublime-ASS
===========

<a href="https://packagecontrol.io/packages/Advanced%20Substation%20Alpha%20(ASS)"><img alt="Package Control" src="https://img.shields.io/packagecontrol/dt/Advanced%20Substation%20Alpha%20(ASS)"></a>
<a href="https://github.com/jfcherng/Sublime-ASS/tags"><img alt="GitHub tag (latest SemVer)" src="https://img.shields.io/github/tag/jfcherng/Sublime-ASS?logo=github"></a>
<a href="https://github.com/jfcherng/Sublime-ASS/blob/master/LICENSE"><img alt="Project license" src="https://img.shields.io/github/license/jfcherng/Sublime-ASS?logo=github"></a>
<a href="https://github.com/jfcherng/Sublime-ASS/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/jfcherng/Sublime-ASS?logo=github"></a>
<a href="https://www.paypal.me/jfcherng/5usd" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-blue.svg?logo=paypal" /></a>

ASS/SSA subtitles syntax highlight for Sublime Text 3.

![screenshot](https://raw.githubusercontent.com/jfcherng/Sublime-ASS/gh-pages/images/screenshot/screenshot.png)


## Settings

```javascript
{
    // when to show a color phantom beside a color code?
    // can be "never", "always" or "hover"
    "show_color_phantom": "always",
    // the period (in milisecond) that consecutive modifications are treated as typing
    // phantoms will be updated only when the user is not considered typing
    // you can make this value larger if you feel ST gets stucked while typing
    "on_modified_typing_period": 150,
}
```


## Specs

- [SSA/ASS Subtitles](http://www.matroska.org/technical/specs/subtitles/ssa.html)
- [ASS Tags](http://docs.aegisub.org/3.2/ASS_Tags/)


## Contributors

- Jack Cherng ([@jfcherng](https://github.com/jfcherng)): the author of the 1st version syntax
- FichteFoll ([@FichteFoll](https://github.com/FichteFoll)): the author of the 2nd rewritten version syntax
