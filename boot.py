from .plugin import set_up
from .plugin import tear_down

# main plugin classes
from .plugin.commands import *  # noqa: F401, F403


def plugin_loaded() -> None:
    set_up()


def plugin_unloaded() -> None:
    tear_down()
