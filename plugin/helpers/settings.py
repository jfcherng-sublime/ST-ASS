from functools import lru_cache
from typing import Any, Optional
import sublime
import time


@lru_cache
def get_package_name() -> str:
    """
    @brief Getsthe package name.

    @return The package name.
    """

    # anyway, the top module should always be the plugin name
    return __package__.partition(".")[0]


def get_settings_object() -> sublime.Settings:
    return sublime.load_settings("ASS.sublime-settings")


def get_setting(key: str, default: Optional[Any] = None) -> Any:
    return get_settings_object().get(key, default)


def get_timestamp() -> float:
    return time.time()
