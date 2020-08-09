import os
import sys

# stupid python module system
sys.path.append(os.path.join(os.path.dirname(__file__), "libs"))


def set_up() -> None:
    """ plugin_loaded """

    pass


def tear_down() -> None:
    """ plugin_unloaded """

    pass
