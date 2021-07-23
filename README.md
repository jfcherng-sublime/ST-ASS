# ST-ASS

[![Required ST Build](https://img.shields.io/badge/ST-4105+-orange.svg?style=flat-square&logo=sublime-text)](https://www.sublimetext.com)
[![GitHub Actions](https://img.shields.io/github/workflow/status/jfcherng-sublime/ST-ASS/Python?style=flat-square)](https://github.com/jfcherng-sublime/ST-ASS/actions)
[![Package Control](https://img.shields.io/packagecontrol/dt/Advanced%20Substation%20Alpha%20%28ASS%29?style=flat-square)](https://packagecontrol.io/packages/Advanced%20Substation%20Alpha%20%28ASS%29)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/jfcherng-sublime/ST-ASS?style=flat-square&logo=github)](https://github.com/jfcherng-sublime/ST-ASS/tags)
[![Project license](https://img.shields.io/github/license/jfcherng-sublime/ST-ASS?style=flat-square&logo=github)](https://github.com/jfcherng-sublime/ST-ASS/blob/st4/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/jfcherng-sublime/ST-ASS?style=flat-square&logo=github)](https://github.com/jfcherng-sublime/ST-ASS/stargazers)
[![Donate to this project using Paypal](https://img.shields.io/badge/paypal-donate-blue.svg?style=flat-square&logo=paypal)](https://www.paypal.me/jfcherng/5usd)

ASS/SSA subtitles syntax highlight for Sublime Text.

![screenshot](https://raw.githubusercontent.com/jfcherng-sublime/ST-ASS/gh-pages/images/screenshot/screenshot.png)

## Settings

```javascript
{
    // when to show a color phantom beside a color code?
    // can be "never", "always" or "hover"
    "show_color_phantom": "always",
    // the period (in millisecond) that consecutive modifications are treated as typing
    // phantoms will be updated only when the user is not considered typing
    // you can make this value larger if you feel ST gets stuck while typing
    "on_modified_typing_period": 150,
}
```

## Specs

- [SSA/ASS Subtitles](http://www.matroska.org/technical/specs/subtitles/ssa.html)
- [ASS Tags](http://docs.aegisub.org/3.2/ASS_Tags/)

## Contributors

- Jack Cherng ([@jfcherng](https://github.com/jfcherng)): the author of the 1st version syntax
- FichteFoll ([@FichteFoll](https://github.com/FichteFoll)): the author of the 2nd rewritten version syntax
