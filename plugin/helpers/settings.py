from typing import Any, Optional
import sublime
import time


def get_package_name() -> str:
    """
    @brief Getsthe package name.

    @return The package name.
    """

    # anyway, the top module should always be the plugin name
    return __package__.partition(".")[0]


def get_package_path() -> str:
    """
    @brief Gets the package path.

    @return The package path.
    """

    return "Packages/" + get_package_name()


def get_settings_file() -> str:
    """
    @brief Get the settings file name.

    @return The settings file name.
    """

    return get_package_name() + ".sublime-settings"


def get_settings_object() -> sublime.Settings:
    return sublime.load_settings(get_settings_file())


def get_setting(key: str, default: Optional[Any] = None) -> Any:
    return get_settings_object().get(key, default)


def get_timestamp() -> float:
    return time.time()
