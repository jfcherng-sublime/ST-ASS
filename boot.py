from .plugin import set_up, tear_down

# main plugin classes
from .plugin.sublime_text.AssColorPhantom import *
from .plugin.sublime_text.AssToggleComment import *


def plugin_loaded() -> None:
    set_up()


def plugin_unloaded() -> None:
    tear_down()
